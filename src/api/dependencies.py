from repositories.questions import QuestionsRepository
from services.questions import QuestionsService
from repositories.topics import TopicsRepository
from services.topics import TopicsService
from services.auth import fastapi_users


def questions_service():
    return QuestionsService(QuestionsRepository)


def topics_service():
    return TopicsService(TopicsRepository)


current_user = fastapi_users.current_user()
current_superuser = fastapi_users.current_user(active=True, superuser=True)
