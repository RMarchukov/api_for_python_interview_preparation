from schemas.questions import QuestionSchemaAdd, QuestionSchemaEdit
from repositories.questions import QuestionsRepository


class QuestionsService:
    def __init__(self, questions_repository):
        self.questions_repository: QuestionsRepository = questions_repository()

    async def add_question(self, question: QuestionSchemaAdd) -> int:
        question_dict = question.model_dump()
        question_id = await self.questions_repository.add_one(question_dict)
        return question_id

    async def get_questions(self):
        questions = await self.questions_repository.find_all()
        return questions

    async def edit_question(self, id: int, question: QuestionSchemaEdit):
        question_dict = question.model_dump()
        question_id = await self.questions_repository.edit_one(id, question_dict)
        return question_id

    async def delete_question(self, id: int):
        question_id = await self.questions_repository.delete_one(id)
        return question_id
