from pydantic import BaseModel


class TopicSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TopicSchemaAdd(BaseModel):
    name: str


class TopicSchemaEdit(BaseModel):
    name: str
