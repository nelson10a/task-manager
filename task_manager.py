import json


tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn SQL", "completed": False},
    {"id": 3, "title": "Build API", "completed": False}
]
def validate_task_id(task_id):
    #type(int) returns a bool True/False
    if type(task_id) != int:
        raise TypeError("Task ID must be an integer.")

def validate_title(title):
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")
    title = title.strip()
    if title == "":
        raise ValueError("Title cannot be empty.")
    return title


def add_task(tasks, title):
    title = validate_title(title)
    if not tasks:
        task_id = 1
    else:
        task_id = max(task["id"] for task in tasks) + 1
    task = {"id": task_id, "title": title, "completed": False}
    tasks.append(task)
    return task
    

def get_task(tasks, task_id):
    #type(int) returns a bool True/False
    validate_task_id(task_id)
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    return None



def complete_task(tasks, task_id):
    validate_task_id(task_id)
    for task in tasks:
        if task_id == task["id"] and task["completed"]:
            return "already completed"
        
        elif task_id == task["id"]:
            task["completed"] = True
            return "completed"
        
    return "not found"


def delete_task(tasks, task_id):
    validate_task_id(task_id)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return "deleted"
        
    return "not found"

def update_task(tasks, task_id, new_title):
    validate_task_id(task_id)
    new_title = validate_title(new_title)
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            return task
    return None

# add_task(tasks, "Learn FASTAPI")


def load_tasks(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)  #json.load()  → file → Python  json.dump()  → Python → file

    except FileNotFoundError:
        return []
    


def save_tasks(tasks, file_path):
    with open(file_path, "w") as file: # open file for writing
        json.dump(tasks, file) # python list (tasks) is written in JSON