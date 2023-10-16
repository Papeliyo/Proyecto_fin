from fastapi import FastAPI
from model.task_connect import TaskConnection
from schema.task_schema import TaskSchema

app = FastAPI()
conn = TaskConnection()

@app.get("/api/view")
def root():
    items = []
    for data in conn.read_all():
        #print(data)
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["titulo"] = data[1]
        dictionary["descripcion"] = data[2]
        dictionary["fecha_vencimiento"] = data[3]
        dictionary["estado"] = data[4]
        items.append(dictionary)
    return items

@app.post("/api/insert")
def insert(task_data:TaskSchema):
    data = task_data.dict()
    data.pop("id")
    #print(data)
    conn.write(data)

@app.put("/api/update/{titulo}")
def update(task_data:TaskSchema, titulo:str):
    data = task_data.dict()
    data["titulo"] = titulo
    #print(data)
    conn.update(data)


@app.delete("/api/delete/{titulo}")
def delete(titulo:str):
    conn.delete(titulo)