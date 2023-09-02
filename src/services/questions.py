from schemas.questions import QuestionSchemaAdd
from utils.repository import AbstractRepository


class QuestionsService:
    def __init__(self, questions_repository: AbstractRepository):
        self.questions_repository = questions_repository()

    async def add_question(self, question: QuestionSchemaAdd) -> int:
        question_dict = question.model_dump()
        question_id = await self.questions_repository.add_one(question_dict)
        return question_id

    async def get_questions(self):
        questions = await self.questions_repository.find_all()
        return questions
