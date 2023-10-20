from datetime import date
from main import insert, update, delete
from schema.task_schema import TaskSchema

# inserts a new task with valid data
def test_insert_valid_data():

    # Create a valid task data as a TaskSchema object
    task_data = TaskSchema(
        titulo="Task 4",
        descripcion="valid data",
        fecha_vencimiento=date.today(),
        estado="pendiente"
    )

    # Call the insert function
    insert(task_data)

# Update a task with valid data
def test_update_valid_data():

    # Create a mock task_data object
    task_data = TaskSchema(
        titulo="Task 4",
        descripcion="dato para borrar",
        fecha_vencimiento="2023-10-10",
        estado="Completado"
    )

    # Call the update function
    update(task_data, "titulo4")

    # delete a task that exists in the database
def test_delete_existing_task():

    # Call the delete function with an existing task title
    delete("titulo5")

