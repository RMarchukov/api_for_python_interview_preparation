from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: int
    title: str
    answer: str
    topic_id: int

    class Config:
        from_attributes = True


class QuestionSchemaAdd(BaseModel):
    title: str
    answer: str
    topic_id: int


class QuestionSchemaEdit(BaseModel):
    answer: str
