from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from db.db import Base
from schemas.questions import QuestionSchema


class Questions(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    answer: Mapped[str]

    @declared_attr
    def topic_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("topics.id", ondelete="cascade"), nullable=True)

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("users.id", ondelete="cascade"), nullable=True)

    def to_read_model(self) -> QuestionSchema:
        return QuestionSchema(
            id=self.id,
            title=self.title,
            answer=self.answer,
            topic_id=self.topic_id,
            user_id=self.user_id,
        )
