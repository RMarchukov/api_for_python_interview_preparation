from schemas.topics import TopicSchemaAdd, TopicSchemaEdit
from repositories.topics import TopicsRepository


class TopicsService:
    def __init__(self, topics_repository):
        self.topics_repository: TopicsRepository = topics_repository()

    async def add_topic(self, topic: TopicSchemaAdd) -> int:
        topic_dict = topic.model_dump()
        topic_id = await self.topics_repository.add_one(topic_dict)
        return topic_id

    async def get_topics(self):
        topics = await self.topics_repository.find_all()
        return topics

    async def edit_topic(self, id: int, topic: TopicSchemaEdit) -> int:
        topic_dict = topic.model_dump()
        topic_id = await self.topics_repository.edit_one(id, topic_dict)
        return topic_id

    async def delete_topic(self, id: int):
        topic_id = await self.topics_repository.delete_one(id)
        return topic_id

    async def get_one_topic(self, id: int):
        topic = await self.topics_repository.find_one(id=id)
        return topic
