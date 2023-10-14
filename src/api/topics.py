from typing import Annotated
from fastapi import APIRouter, Depends
from api.dependencies import topics_service, current_user
from schemas.topics import TopicSchemaAdd, TopicSchemaEdit
from services.topics import TopicsService


router = APIRouter(
    prefix="/topics",
    tags=["Topics"]
)


@router.post("", dependencies=[Depends(current_user)])
async def add_topic(
    topic: TopicSchemaAdd,
    topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topic_id = await topics_service.add_topic(topic)
    return {"topic_id": topic_id}


@router.get("")
async def get_topics(topics_service: Annotated[TopicsService, Depends(topics_service)]):
    topics = await topics_service.get_topics()
    return topics


@router.patch("", dependencies=[Depends(current_user)])
async def edit_topic(
        id: int,
        topic: TopicSchemaEdit,
        topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topic_id = await topics_service.edit_topic(id, topic)
    return {"topic_id": topic_id}


@router.delete("", dependencies=[Depends(current_user)])
async def delete_topic(
        id: int,
        topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topic_id = await topics_service.delete_topic(id)
    return {"topic_id": topic_id}


@router.get("/one")
async def get_one_topic(
        id: int,
        topics_service: Annotated[TopicsService, Depends(topics_service)]
):
    topic = await topics_service.get_one_topic(id)
    return topic.scalar_one()
