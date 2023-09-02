from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import questions_service
from schemas.questions import QuestionSchemaAdd
from services.questions import QuestionsService


router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.post("")
async def add_question(
    question: QuestionSchemaAdd,
    questions_service: Annotated[QuestionsService, Depends(questions_service)]
):
    question_id = await questions_service.add_question(question)
    return {"question_id": question_id}


@router.get("")
async def get_questions(questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    questions = await questions_service.get_questions()
    return questions
