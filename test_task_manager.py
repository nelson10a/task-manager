from task_manager import complete_task, add_task, get_task, delete_task, load_tasks, save_tasks, update_task
from cli import add_task_cli, list_tasks_cli, complete_task_cli, delete_task_cli, main, update_task_cli
import pytest
import json


@pytest.fixture
def tasks():
    return [

        {"id": 1, "title": "Learn Python", "completed": False},
        {"id": 2, "title": "Learn SQL", "completed": False},
        {"id": 3, "title": "Build API", "completed": False}

        ]
# ============================== COMPLETE TASK ====================================

def test_complete_task(tasks):
    result = complete_task(tasks, 2)

    assert result == "completed"
    # assert tasks[1]["completed"] is True


def test_task_already_completed(tasks):
    complete_task(tasks, 2)
    result = complete_task(tasks, 2)

    assert result == "already completed"

def test_task_not_found(tasks):
    result = complete_task(tasks, 99)

    assert result == "not found"


def test_complete_task_id_type_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        complete_task(tasks, "2")
    assert str(exc_info.value) == "Task ID must be an integer."

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

    assert str(exc_info.value) == "Title cannot be empty."


def test_add_task_title_strip(tasks):
    result = add_task(tasks, " Learn Python ")

    assert result["title"] == "Learn Python"


def test_task_title_white_space_validation(tasks):
    with pytest.raises(ValueError) as exc_info:
        add_task(tasks, " ")
    assert str(exc_info.value) == "Title cannot be empty."


def test_add_task_interger(tasks):
    with pytest.raises(TypeError) as exc_info:
        add_task(tasks, 123)
    assert str(exc_info.value) == "Title must be a string."

# ============================== GET/READ TASK ====================================

def test_get_task(tasks):
    result = get_task(tasks, 2)

    assert result["title"] == "Learn SQL"


def test_get_task_not_found(tasks):
    result = get_task(tasks, 99)

    assert result is None

def test_get_task_id_type_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        get_task(tasks, "2")
    assert str(exc_info.value) == "Task ID must be an integer."


def test_get_task_bool_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        get_task(tasks, True)
    assert str(exc_info.value) == "Task ID must be an integer."

# ============================== DELETE TASK ====================================

def test_delete_task(tasks):
    result = delete_task(tasks, 2)

    assert result == "deleted"
    assert get_task(tasks, 2) is None
    result = delete_task(tasks, 99) 
    assert result == "not found"

def test_delete_task_id_type_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        delete_task(tasks, "1")
    assert str(exc_info.value) == "Task ID must be an integer."



#=====================TEST FOR CLI==========================================

def test_add_task_cli(tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Learn Docker")
    result = add_task_cli(tasks)
    assert result["title"] == "Learn Docker"


def test_list_tasks_cli(tasks, capsys):
    list_tasks_cli(tasks)

    captured = capsys.readouterr()
    assert "Learn Python" in captured.out
    assert "Learn SQL" in captured.out
    assert "Build API" in captured.out

# Test for Update task CLI
def test_update_task_cli(tasks, monkeypatch):
    answers = iter(["1", "Learn FASTAPI"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    result = update_task_cli(tasks)
    assert result["id"] == 1
    assert result["title"] == "Learn FASTAPI"
    
def test_update_task_cli_input_validation(tasks, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    update_task_cli(tasks)
    captured = capsys.readouterr()
    assert "Task ID must be an integer." in captured.out

def test_update_task_cli_not_found(tasks, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "99")
    update_task_cli(tasks)
    captured = capsys.readouterr()
    assert "Task not found" in captured.out



def test_list_tasks_not_completed(tasks, capsys):
    list_tasks_cli(tasks)

    captured = capsys.readouterr()
    assert "completed" in captured.out
    assert "completed" in captured.out
    assert "completed" in captured.out


 # Always remember, your test name always reminds you what you are testing for,
 # and what it should return or assert 
def test_complete_task_cli(tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 2)
    result = complete_task_cli(tasks)
    assert result == "completed"
    assert tasks[1]["completed"] is True


def test_complete_task_not_int_validation(tasks, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    complete_task_cli(tasks)
    captured = capsys.readouterr()
    assert "Task ID must be an integer." in captured.out



def test_delete_task_cli(tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    result = delete_task_cli(tasks)
    assert result == "deleted"
    assert get_task(tasks, 2) is None


def test_delete_task_cli_not_found(tasks, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "99")
    result = delete_task_cli(tasks)
    assert result == "not found"
    assert len(tasks) == 3


def test_delete_task_cli_invalid_input(tasks, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    delete_task_cli(tasks)
    captured = capsys.readouterr()
    assert "Task ID must be an integer." in captured.out
    assert len(tasks) == 3


# AUTOMATED TESTING/Integration tests
def test_main_add_and_list_task(monkeypatch, capsys, tmp_path):
    answer = iter(["1", "Learn Docker", "2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(answer))
    file_path = tmp_path / "tasks.json"
    main(file_path)
    captured = capsys.readouterr()
    assert "Learn Docker" in captured.out
    assert "Goodbye" in captured.out



def test_main_complete_and_delete_task(monkeypatch, capsys, tmp_path):
    answers = iter(["1", "Learn Python", "1", "Learn Docker", "3", "1", "4", "2", "2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    file_path = tmp_path / "tasks.json"
    main(file_path)
    captured = capsys.readouterr()
    assert "Learn Python completed" in captured.out
    assert "Learn Docker" not in captured.out
    assert "Goodbye" in captured.out


def test_load_tasks_returns_empty_list_when_file_missing(tmp_path):
    file_path = tmp_path / "tasks.json"
    result = load_tasks(file_path)

    assert result == []


def test_load_tasks_returns_saved_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    expected_tasks = [
        {"id": 1, "title": "Learn Python", "completed": False}
    ]
    with open(file_path, "w") as file:
        json.dump(expected_tasks, file)
    result = load_tasks(file_path)
    assert result == expected_tasks



def test_save_tasks_write_tasks_to_file(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [
        {"id": 1, "title": "Learn Python", "completed": False}
    ]
    save_tasks(tasks, file_path) # wrote file in file_path as JSON
    with open(file_path, "r") as file:  # reads open file in file_path
        loaded_task = json.load(file)  # loads file whilst open to python list/dict
    assert loaded_task == tasks  # confirms loaded_tasks in dic/list contains the same task of tasks in dict/list
    


def test_update_task_title(tasks):
    tasks[0]["title"] = "Learn Pythn"
    result = update_task(tasks, 1, "Learn Python")
    assert result["title"] == "Learn Python"
    assert tasks[0]["title"] == "Learn Python"


def test_update_task_id_does_not_exist(tasks):
    result = update_task(tasks, 99, "Learn Python")
    assert result is None


def test_update_task_id_not_integer_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        update_task(tasks, "1", "Learn Python")
    assert str(exc_info.value) == "Task ID must be an integer."


def test_new_title_update_not_string_validation(tasks):
    with pytest.raises(TypeError) as exc_info:
        update_task(tasks, 1, 123)
    assert str(exc_info.value) == "Title must be a string."

def  test_new_title_empty_validation(tasks):
    with pytest.raises(ValueError) as exc_info:
        update_task(tasks, 1, "   ")
    assert str(exc_info.value) == "Title cannot be empty."


def test_main_integration_for_update(monkeypatch, capsys, tmp_path):
    answers = iter(["1","Gearbx", "5", "1", "Gearbox", "2", "6"])
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    main(file_path)
    captured = capsys.readouterr()
    assert "Gearbx" not in captured.out
    assert "Gearbox" in captured.out


def test_main_integration_for_complete_task_after_restart(monkeypatch, capsys, tmp_path):
    first_run = iter(["1", "Gearbox", "3", "1", "6"])
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr("builtins.input", lambda _: next(first_run))
    main(file_path)
    second_run = iter(["2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(second_run))
    main(file_path)
    captured = capsys.readouterr()
    assert "Gearbox completed" in captured.out


def test_main_integration_for_delete_task_after_restart(monkeypatch, capsys, tmp_path):
    first_run = iter(["1", "Gearbox", "4", "1", "6"])
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr("builtins.input", lambda _: next(first_run))
    main(file_path)
    second_run = iter(["2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(second_run))
    main(file_path)
    captured = capsys.readouterr()
    assert "Gearbox" not in captured.out


def test_main_integration_for_update_after_restart(monkeypatch, capsys, tmp_path):
    first_run = iter(["1", "Gearbx", "5", "1", "Gearbox", "6"])
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr("builtins.input", lambda _: next(first_run))
    main(file_path)
    second_run = iter(["2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(second_run))
    main(file_path)
    captured = capsys.readouterr()
    assert "Gearbox" in captured.out
    assert "Gearbox" not in captured.out