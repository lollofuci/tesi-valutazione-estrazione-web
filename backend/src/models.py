from pydantic import BaseModel

class ParseResponse(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    parsed_text: str

class DomainsResponse(BaseModel):
    domains: list[str]


class GoldStandardEntry(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    gold_text: str


class FullGoldStandardResponse(BaseModel):
    gold_standard: list[GoldStandardEntry]


class EvalRequest(BaseModel):
    parsed_text: str
    gold_text: str


class MetricScores(BaseModel):
    precision: float
    recall: float
    f1: float


class EvalResponse(BaseModel):
    token_level_eval: MetricScores
    x_eval: dict