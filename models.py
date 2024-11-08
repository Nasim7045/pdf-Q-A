# app/models.py
from pydantic import BaseModel

class Document(BaseModel):
    filename: str
    text: str
    upload_date: str = None
