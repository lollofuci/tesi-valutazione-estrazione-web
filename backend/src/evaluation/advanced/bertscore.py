"""BERTScore (Zhang et al., 2020) adattato a documenti lunghi.

BERTScore confronta i due testi nello spazio degli embedding contestuali di un modello
Transformer: ogni token del testo estratto viene abbinato al token piu' simile (coseno)
del Gold Standard e viceversa.
- Precision = media, sui token estratti, della massima similarita' con il Gold Standard
- Recall    = media, sui token del Gold Standard, della massima similarita' con l'estratto

La libreria di riferimento `bert-score` tronca ogni testo a 512 token: su una pagina di
Wikipedia (decine di migliaia di token) valuterebbe solo l'inizio. Qui il testo viene
diviso in blocchi da 510 token, ogni blocco viene codificato separatamente e le
similarita' vengono calcolate su tutti i token, a blocchi per contenere la memoria.

Modello predefinito: bert-base-multilingual-cased, strato 9 (la scelta di `bert-score`
per questo modello), perche' i domini sono in parte in italiano e in parte in inglese.
"""

from __future__ import annotations

import hashlib
import os

DEFAULT_MODEL = os.getenv("BERTSCORE_MODEL", "bert-base-multilingual-cased")
DEFAULT_LAYER = int(os.getenv("BERTSCORE_LAYER", "9"))


class LongBertScorer:
    def __init__(self, model_name: str = DEFAULT_MODEL, layer: int = DEFAULT_LAYER,
                 chunk_tokens: int = 510, batch_size: int = 8, sim_block: int = 2048) -> None:
        self.model_name = model_name
        self.layer = layer
        self.chunk_tokens = chunk_tokens
        self.batch_size = batch_size
        self.sim_block = sim_block
        self._tokenizer = None
        self._model = None
        self._cache: dict[str, object] = {}

    # -- caricamento pigro: torch e transformers servono solo se si usa BERTScore --
    def _load(self) -> None:
        if self._model is not None:
            return
        import torch
        from transformers import AutoModel, AutoTokenizer
        from transformers.utils import logging as hf_logging

        hf_logging.set_verbosity_error()
        self._torch = torch
        self._tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self._model = AutoModel.from_pretrained(self.model_name, output_hidden_states=True)
        self._model.eval()

    def _embed(self, text: str, cache: bool = False):
        """Embedding normalizzati (n_token x dim) di tutto il testo, senza [CLS]/[SEP].

        Con cache=True il risultato viene memorizzato: si usa per i Gold Standard, che
        vengono confrontati con molte varianti dello stesso documento.
        """
        key = hashlib.sha1(text.encode("utf-8")).hexdigest()
        if key in self._cache:
            return self._cache[key]
        torch = self._torch
        tok = self._tokenizer
        ids = tok(text, add_special_tokens=False, verbose=False)["input_ids"]
        if not ids:
            return torch.zeros((0, self._model.config.hidden_size))

        chunks = [ids[i:i + self.chunk_tokens] for i in range(0, len(ids), self.chunk_tokens)]
        pieces = []
        with torch.no_grad():
            for start in range(0, len(chunks), self.batch_size):
                batch = chunks[start:start + self.batch_size]
                seqs = [[tok.cls_token_id] + c + [tok.sep_token_id] for c in batch]
                max_len = max(len(s) for s in seqs)
                input_ids = torch.full((len(seqs), max_len), tok.pad_token_id, dtype=torch.long)
                attention = torch.zeros((len(seqs), max_len), dtype=torch.long)
                for row, seq in enumerate(seqs):
                    input_ids[row, :len(seq)] = torch.tensor(seq)
                    attention[row, :len(seq)] = 1
                hidden = self._model(input_ids=input_ids, attention_mask=attention).hidden_states[self.layer]
                for row, seq in enumerate(seqs):
                    pieces.append(hidden[row, 1:len(seq) - 1])  # esclude [CLS] e [SEP]
        emb = torch.cat(pieces, dim=0)
        emb = torch.nn.functional.normalize(emb, dim=-1)
        if cache:
            self._cache[key] = emb
        return emb

    def score(self, parsed_text: str, gold_text: str) -> dict[str, float]:
        from evaluation.advanced.text_utils import normalize_text

        self._load()
        torch = self._torch
        cand = self._embed(normalize_text(parsed_text))
        ref = self._embed(normalize_text(gold_text), cache=True)
        if cand.shape[0] == 0 or ref.shape[0] == 0:
            return {"precision": 0.0, "recall": 0.0, "f": 0.0}

        row_max_sum = 0.0
        col_max = torch.full((ref.shape[0],), -1.0)
        with torch.no_grad():
            for start in range(0, cand.shape[0], self.sim_block):
                sims = cand[start:start + self.sim_block] @ ref.T
                row_max_sum += sims.max(dim=1).values.sum().item()
                col_max = torch.maximum(col_max, sims.max(dim=0).values)
        precision = row_max_sum / cand.shape[0]
        recall = col_max.mean().item()
        f = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0.0
        return {"precision": precision, "recall": recall, "f": f}

    def clear_cache(self) -> None:
        self._cache.clear()
