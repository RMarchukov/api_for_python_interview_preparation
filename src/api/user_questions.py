from models.auth import Users
from fastapi import APIRouter, Depends, Response, status
from api.dependencies import questions_service, current_user
from typing import Annotated
from services.questions import QuestionsService
from schemas.questions import UserQuestionSchemaAdd, QuestionSchemaEdit
from sqlalchemy.exc import NoResultFound

router = APIRouter(
    prefix="/user/questions",
    tags=["User Questions"],
)


@router.get("", dependencies=[Depends(current_user)])
async def get_user_questions(questions_service: Annotated[QuestionsService, Depends(questions_service)],
                             user: Users = Depends(current_user)):
    questions = await questions_service.get_user_questions(user.id)
    return questions


@router.post("", dependencies=[Depends(current_user)])
async def add_user_question(question: UserQuestionSchemaAdd,
                            questions_service: Annotated[QuestionsService, Depends(questions_service)],
                            user: Users = Depends(current_user)):
    question_id = await questions_service.add_user_question(question, user.id)
    return {"question_id": question_id}


@router.patch("", dependencies=[Depends(current_user)])
async def edit_user_question(id: int,
                             question: QuestionSchemaEdit,
                             questions_service: Annotated[QuestionsService, Depends(questions_service)],
                             user: Users = Depends(current_user),
                             response: Response = status.HTTP_200_OK):
    try:
        question_id = await questions_service.edit_user_question(id, user.id, question)
        return {"question_id": question_id}
    except NoResultFound:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response


@router.delete("", dependencies=[Depends(current_user)])
async def delete_user_question(id: int,
                               questions_service: Annotated[QuestionsService, Depends(questions_service)],
                               user: Users = Depends(current_user),
                               response: Response = status.HTTP_200_OK):
    try:
        question_id = await questions_service.delete_user_question(id, user.id)
        return {"question_id": question_id}
    except NoResultFound:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response
