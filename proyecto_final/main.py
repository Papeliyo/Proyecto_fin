from fastapi import FastAPI
from model.task_connect import TaskConnection
from schema.task_schema import TaskSchema

app = FastAPI()
conn = TaskConnection()


@app.get("/")
def root():
    conn
    return {"Hi, i am fastAPI"}

@app.post("/api/insert")
def insert(task_data:TaskSchema):
    data = task_data.dict()
    data.pop("id")
    print(data)