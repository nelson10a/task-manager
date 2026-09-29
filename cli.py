from task_manager import add_task, complete_task, delete_task




def add_task_cli(tasks):
    title = input("Enter task title: ")
    task = add_task(tasks, title)
    return task


def list_tasks_cli(tasks):
    for task in tasks:
        if task["completed"]:
            print(task["title"],"completed" )
        else:
            print(task["title"], "Not completed")

    
def complete_task_cli(tasks):
    try:
        task_id = int(input("Enter Task ID to complete: "))
    except ValueError:
        print("Task ID must be an integer")
        return
    result = complete_task(tasks, task_id)
    return result


def delete_task_cli(tasks):
    try:  
        task_id = int(input("Enter a Task ID: "))
    except ValueError:
        print("Task ID must be an integer.")
        return
    result = delete_task(tasks, task_id)
    return result