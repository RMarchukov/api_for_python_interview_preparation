from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.topics import TopicSchema


class Topics(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_read_model(self) -> TopicSchema:
        return TopicSchema(
            id=self.id,
            name=self.name,
        )
