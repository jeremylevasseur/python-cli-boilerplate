from pydantic import BaseModel


class TyperMetadata(BaseModel):
    name: str
    help: str
