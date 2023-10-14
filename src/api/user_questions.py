from schemas.auth import UserRead
from fastapi import APIRouter, Depends
from api.dependencies import questions_service, current_user
from typing import Annotated
from services.questions import QuestionsService
from schemas.questions import UserQuestionSchemaAdd

router = APIRouter(
    prefix="/user/questions",
    tags=["User Questions"],
)


@router.get("", dependencies=[Depends(current_user)])
async def get_user_questions(questions_service: Annotated[QuestionsService, Depends(questions_service)],
                             user: UserRead = Depends(current_user)):
    questions = await questions_service.get_user_questions(user.id)
    return questions


@router.post("", dependencies=[Depends(current_user)])
async def add_user_question(question: UserQuestionSchemaAdd,
                            questions_service: Annotated[QuestionsService, Depends(questions_service)],
                            user: UserRead = Depends(current_user)):
    question_id = await questions_service.add_user_question(question, user.id)
    return {"question_id": question_id}
