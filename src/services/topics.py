from schemas.topics import TopicSchemaAdd
from utils.repository import AbstractRepository


class TopicsService:
    def __init__(self, topics_repository: AbstractRepository):
        self.topics_repository: AbstractRepository = topics_repository()

    async def add_topic(self, topic: TopicSchemaAdd) -> int:
        topic_dict = topic.model_dump()
        topic_id = await self.topics_repository.add_one(topic_dict)
        return topic_id

    async def get_topics(self):
        topics = await self.topics_repository.find_all()
        return topics
