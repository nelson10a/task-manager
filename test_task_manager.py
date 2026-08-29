from task_manager import complete_task
import pytest


@pytest.fixture
def tasks():
    return [
        {"title": "Learn Python", "completed": False},
        {"title": "Learn SQL", "completed": False},
        {"title": "Build API", "completed": False}
    ]


def test_complete_task(tasks):
    result = complete_task(tasks,"Learn Python")

    assert result == "completed"


def test_task_not_found(tasks):
    result = complete_task(tasks, "Learn Java")

    assert result == "not found"
    


def test_task_already_completed(tasks):
    complete_task(tasks, "Learn Python")
    result = complete_task(tasks, "Learn Python")

    assert result == "already completed"