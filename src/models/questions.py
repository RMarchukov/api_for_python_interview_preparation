from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base
from schemas.questions import QuestionSchema


class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    answer: Mapped[str]
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))

    def to_read_model(self) -> QuestionSchema:
        return QuestionSchema(
            id=self.id,
            title=self.title,
            answer=self.answer,
            topic_id=self.topic_id,
        )
