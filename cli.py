from task_manager import add_task




def add_task_cli(tasks):
    title = input("Enter task title: ")
    task = add_task(tasks, title)
    return task