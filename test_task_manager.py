from task_manager import complete_task, add_task, get_task, delete_task
import pytest


@pytest.fixture
def tasks():
    return [

        {"id": 1, "title": "Learn Python", "completed": False},
        {"id": 2, "title": "Learn SQL", "completed": False},
        {"id": 3, "title": "Build API", "completed": False}

        ]
# ============================== COMPLETE TASK ====================================

def test_complete_task(tasks):
    result = complete_task(tasks,2)

    assert result == "completed"
    # assert tasks[1]["completed"] is True



def test_task_already_completed(tasks):
    complete_task(tasks, 2)
    result = complete_task(tasks, 2)

    assert result == "already completed"

def test_task_not_found(tasks):
    result = complete_task(tasks, 99)

    assert result == "not found"
    
# ============================== ADD TASK ====================================

def test_add_task(tasks):
    result = add_task(tasks, "Learn FASTAPI")

    assert result["title"] == "Learn FASTAPI"
    assert result["completed"] is False
    assert len(tasks) == 4


def test_add_task_id_increment(tasks):
    result = add_task(tasks, "Learn SQL")

    assert result["id"] == 4


def test_add_task_after_delete(tasks):
    delete_task(tasks, 2)
    result = add_task(tasks, "Learn FASTAPI")
    assert result["id"] == 4

    # assert tasks[-1]["id"] == 3




def test_add_task_empty_list():
    tasks =[]
    result = add_task(tasks, "Learn Python")

    assert result["id"] == 1
    assert result["title"] == "Learn Python"
    assert result["completed"] is False

# Testing  exception handling with pytest.raises
def test_add_task_empty_title(tasks):
    with pytest.raises(ValueError) as exc_info:
        add_task(tasks, "")

    assert str(exc_info.value) == "Title cannot be empty"



# ============================== GET/READ TASK ====================================

def test_get_task(tasks):
    result = get_task(tasks, 2)

    assert result["title"] == "Learn SQL"


def test_get_task_not_found(tasks):
    result = get_task(tasks, 99)

    assert result is None


# ============================== DELETE TASK ====================================

def test_delete_task(tasks):
    result = delete_task(tasks, 2)

    assert result == "deleted"
    assert get_task(tasks, 2) is None
    result =  delete_task(tasks, 99) 
    assert result == "not found"

