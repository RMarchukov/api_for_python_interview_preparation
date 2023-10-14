from schemas.questions import QuestionSchemaAdd, QuestionSchemaEdit, UserQuestionSchemaAdd
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

    async def get_one_question(self, id: int):
        question = await self.questions_repository.find_one(id=id)
        return question

    async def get_user_questions(self, user_id: int):
        questions = await self.questions_repository.find_all_by_user(user_id=user_id)
        return questions

    async def add_user_question(self, question: UserQuestionSchemaAdd, user_id: int) -> int:
        question_dict = question.model_dump()
        question_dict.update({"user_id": user_id})
        question_id = await self.questions_repository.add_one_by_user(question_dict)
        return question_id
