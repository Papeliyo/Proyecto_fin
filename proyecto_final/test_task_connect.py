from datetime import date
from main import insert, update, delete, update_state
from schema.task_schema import TaskSchema
from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.fixture
def client():
    # Create a test client for FastAPI app
    client = TestClient(app)
    return client

def test_root(client):
    # Call the root endpoint
    response = client.get("/api/view")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response is a JSON list
    assert isinstance(response.json(), list)

# inserts a new task with valid data
def test_insert_valid_data():

    # Create a valid task data as a TaskSchema object
    task_data = TaskSchema(
        titulo="titulo5",
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
        titulo="titulo5",
        descripcion="dato para borrar",
        fecha_vencimiento="2023-10-10",
        estado="Completado"
    )

    # Call the update function
    update(task_data, "titulo4")

# Update_state a task with valid data
def test_update_state_valid_data():

    # Create a mock task_data object
    task_data = TaskSchema(
        titulo="titulo5",
        descripcion="dato para borrar",
        fecha_vencimiento="2023-10-10",
        estado="Pendiente"
    )

    # Call the update function
    update_state(task_data, "titulo4")

# delete a task that exists in the database
def test_delete_existing_task():

    # Call the delete function with an existing task title
    delete("titulo5")