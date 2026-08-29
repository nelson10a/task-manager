


tasks = [
    {"title": "Learn Python", "completed": False},
    {"title": "Learn SQL", "completed": False},
    {"title": "Build API", "completed": False}
]


def complete_task(task, task_to_complete):
    for task in tasks:
        if task_to_complete == task["title"] and task["completed"]:
            return "already completed"
        
        elif task_to_complete == task["title"]:
            task["completed"] = True
            return "completed"
        
    return "not found"