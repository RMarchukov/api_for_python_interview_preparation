import uvicorn
from fastapi import FastAPI
from api.routers import all_routers


app = FastAPI(
    title="python_interview_preparation"
)


@app.get('/')
def hello():
    return {"description": "API_for_python_interview_preparation"}


for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
