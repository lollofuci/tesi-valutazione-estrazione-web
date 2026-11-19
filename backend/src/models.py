from pydantic import BaseModel
from typing import List, Optional


class ParseResponse(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    parsed_text: str


class DomainsResponse(BaseModel):
    domains: List[str]


class GoldStandardEntry(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    gold_text: str


class FullGoldStandardResponse(BaseModel):
    gold_standard: List[GoldStandardEntry]


class ParseHtmlRequest(BaseModel):
    url: str
    html_text: str


class ParseRequest(BaseModel):
    url: str
    local: Optional[bool] = None


class EvalRequest(BaseModel):
    parsed_text: str
    gold_text: str


class EvalMetrics(BaseModel):
    precision: float
    recall: float
    f1: float


class EvalResponse(BaseModel):
    token_level_eval: EvalMetrics
    x_eval: dict


class JudgeResponse(BaseModel):
    model_name: str
    judge_score: int
    judge_feedback: str


class FullGsEvalResponse(BaseModel):
    token_level_eval: EvalMetrics
    judge_score: float
    x_eval: dict