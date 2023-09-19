from api.questions import router as router_questions
from api.topics import router as router_topics
from api.auth import auth_routers

all_routers = [
    router_questions,
    router_topics,
    auth_routers
]
