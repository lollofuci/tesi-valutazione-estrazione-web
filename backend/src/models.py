from pydantic import BaseModel


class ParsedDocument(BaseModel):
    url: str
    domain: str
    title: str
    html_text: str
    parsed_text: str