from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from api.dependencies import questions_service, current_superuser
from schemas.questions import QuestionSchemaAdd, QuestionSchemaEdit
from services.questions import QuestionsService

router = APIRouter(
    prefix="/questions",
    tags=["Questions"],
)


@router.post("", dependencies=[Depends(current_superuser)])
async def add_question(question: QuestionSchemaAdd,
                       questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    question_id = await questions_service.add_question(question)
    return {"question_id": question_id}


@router.get("")
@cache(expire=600)
async def get_questions(questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    questions = await questions_service.get_questions()
    return questions


@router.patch("", dependencies=[Depends(current_superuser)])
async def edit_question(id: int,
                        question: QuestionSchemaEdit,
                        questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    question_id = await questions_service.edit_question(id, question)
    return {"question_id": question_id}


@router.delete("", dependencies=[Depends(current_superuser)])
async def delete_question(id: int, questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    question_id = await questions_service.delete_question(id)
    return {"question_id": question_id}


@router.get("/one")
async def get_one_question(id: int, questions_service: Annotated[QuestionsService, Depends(questions_service)]):
    question = await questions_service.get_one_question(id)
    res = question.scalar_one()
    return res
