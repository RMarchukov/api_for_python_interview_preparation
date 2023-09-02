from models.questions import Questions
from utils.repository import SQLAlchemyRepository


class QuestionsRepository(SQLAlchemyRepository):
    model = Questions
