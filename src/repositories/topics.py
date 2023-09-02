from models.topics import Topics
from utils.repository import SQLAlchemyRepository


class TopicsRepository(SQLAlchemyRepository):
    model = Topics
