from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import topics_service
from schemas.topics import TopicSchemaAdd
from services.topics import TopicsService


router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)


@router.post("")
async def add_topic(
    topic: TopicSchemaAdd,
    topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topic_id = await topics_service.add_topic(topic)
    return {"topic_id": topic_id}


@router.get("")
async def get_topics(
    topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topics = await topics_service.get_topics()
    return topics
