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
    """
    Inserta una tarea en la base de datos.

    Args:
    - task_data: Los datos de la tarea a insertar.

    Example:
    ```json
    {
        "titulo": "Tarea de ejemplo",
        "descripcion": "Esta es una tarea de ejemplo.",
        "fecha_vencimiento": "2023-10-31",
        "estado": "Pendiente o Completado"
    }
    ```

    Returns:
    Los datos de la tarea insertada.
    """
    data = task_data.dict()
    data.pop("id")
    #print(data)
    conn.write(data)

@app.put("/api/update/{titulo}")
def update(task_data:TaskSchema, titulo:str):
    """
    Actualizar una tarea en la base de datos.

    Args:
    - task_data: Los datos de la tarea en actualizar.
    - titulo: El titulo de la tarea en actualizar

    Example:
    ```json
    {
        "titulo": "Tarea de ejemplo",
        "descripcion": "Esta es una tarea de ejemplo.",
        "fecha_vencimiento": "2023-10-31",
        "estado": "Pendiente o Completado"
    }
    ```

    Returns:
    Los datos de la tarea seran actualizados.
    """
    data = task_data.dict()
    data["titulo"] = titulo
    #print(data)
    conn.update(data)

@app.put("/api/update_state/{titulo}")
def update_state(task_data:TaskSchema, titulo:str):
    """
    Actualizar el estado de una tarea en la base de datos.

    Args:
    - task_data: Los datos de la tarea en actualizar.
    - titulo: El titulo de la tarea en actualizar

    Example:
    ```json
    {
        "titulo": "Tarea de ejemplo",
        "descripcion": "Esta es una tarea de ejemplo.",
        "fecha_vencimiento": "2023-10-31",
        "estado": "Pendiente o Completado"
    }
    ```

    Returns:
    El estado de la tarea sera actualizado.
    """
    data = task_data.dict()
    data["titulo"] = titulo
    #print(data)
    conn.update_state(data)

@app.delete("/api/delete/{titulo}")
def delete(titulo:str):
    """
    Eliminar una tarea en la base de datos.

    Args:
    - titulo: El titulo de la tarea en actualizar

    Example:
    ```json
    {
    }
    ```

    Returns:
    Tarea eliminada.
    """
    conn.delete(titulo)