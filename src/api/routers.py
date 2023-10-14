from api.questions import router as router_questions
from api.topics import router as router_topics
from api.auth import auth_routers
from api.user_questions import router as router_user_questions

all_routers = [
    router_questions,
    router_topics,
    auth_routers,
    router_user_questions,
]
