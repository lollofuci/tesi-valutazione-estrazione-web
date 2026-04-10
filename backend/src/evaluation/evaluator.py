
#Funzione che ritorna il testo 'tokenizzato'
def tokenized_text(text: str) -> set[str]:
    return set(text.lower().split())




#Funzione che restituisce la qualità del testo parsato
#Confronto tra parsed e gold -> OUTPUT: dizionario
def token_level_eval(parsed_text: str, gold_text: str) -> dict[str, float]:
    parsed_token = tokenized_text(parsed_text)
    golden_token = tokenized_text(gold_text)

    intersection = parsed_token & golden_token

    #Precision = |tokens_estratti ∩ tokens_gs| / |tokens_estratti|

    precision = 0.0
    if parsed_token:
        precision = len(intersection) / len(parsed_token)

    #|tokens_estratti ∩ tokens_gs| / |tokens_gs|

    recall = 0.0
    if golden_token:
        recall = len(intersection) / len(golden_token)

    #F1 = 2 × precision × recall / (precision + recall)

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)
    
    return {
        "precision" : precision,
        "recall" : recall,
        "f1" : f1
    }





#FUNZIONE CHE RESTITUISCE LA MEDIA FINALE:
def aggregate_metrics(metrics_list: list[dict[str, float]]) -> dict[str, float]:
    if not metrics_list:
        return {
            "precision" : 0.0,
            "recall" : 0.0,
            "f1" : 0.0
        }
    
    #calcolo valori output:
    sommap = 0.0
    for m in metrics_list:
        sommap += m["precision"]
    precisionM = sommap / len(metrics_list)

    sommar = 0.0
    for m in metrics_list:
        sommar += m["recall"]
    recallM = sommar / len(metrics_list)

    sommaf = 0.0
    for m in metrics_list:
        sommaf += m["f1"]
    f1M = sommaf / len(metrics_list)

    return {
        "precision" : precisionM,
        "recall" : recallM,
        "f1" : f1M
    }

    

    





    


