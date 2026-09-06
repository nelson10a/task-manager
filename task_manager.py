


tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn SQL", "completed": False},
    {"id": 3, "title": "Build API", "completed": False}
]



def add_task(tasks, title):
    title = title.strip()
    if title == "":
        raise ValueError("Title cannot be empty")
    
    if not tasks:
        task_id = 1
    else:
        task_id = max(task["id"] for task in tasks) + 1
    task = {"id": task_id, "title": title, "completed": False}
    tasks.append(task)
    return task
    

def get_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    
    return None


def complete_task(tasks, task_id):
    for task in tasks:
        if task_id == task["id"] and task["completed"]:
            return "already completed"
        
        elif task_id == task["id"]:
            task["completed"] = True
            return "completed"
        
    return "not found"


def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return "deleted"
        
    return "not found"


# add_task(tasks, "Learn FASTAPI")
