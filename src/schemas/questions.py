from typing import Union

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: int
    title: str
    answer: str
    topic_id: Union[int, None]
    user_id: Union[int, None]

    class Config:
        from_attributes = True


class QuestionSchemaAdd(BaseModel):
    title: str
    answer: str
    topic_id: Union[int, None]


class QuestionSchemaEdit(BaseModel):
    title: str
    answer: str


class UserQuestionSchemaAdd(BaseModel):
    title: str
    answer: str
