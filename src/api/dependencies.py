from repositories.questions import QuestionsRepository
from services.questions import QuestionsService
from repositories.topics import TopicsRepository
from services.topics import TopicsService


def questions_service():
    return QuestionsService(QuestionsRepository)


def topics_service():
    return TopicsService(TopicsRepository)
