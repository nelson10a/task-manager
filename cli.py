from task_manager import add_task, complete_task, delete_task, load_tasks, save_tasks, update_task




def add_task_cli(tasks):
    title = input("Enter task title: ")
    task = add_task(tasks, title)
    return task


def list_tasks_cli(tasks):
    for task in tasks:
        if task["completed"]:
            print(task["title"],"completed." )
        else:
            print(task["title"], "Not completed.")

    
def complete_task_cli(tasks):
    try:
        task_id = int(input("Enter Task ID to complete: "))
    except ValueError:
        print("Task ID must be an integer.")
        return
    result = complete_task(tasks, task_id)
    return result


# Update Task for Client
def update_task_cli(tasks):
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Task ID must be an integer.")
        return
    new_title = input("Enter new title: ")
    result = update_task(tasks, task_id, new_title)
    if result is None:
        print("Task not found.")
    else:
        return result



def delete_task_cli(tasks):
    try:  
        task_id = int(input("Enter a Task ID: "))
    except ValueError:
        print("Task ID must be an integer.")
        return
    result = delete_task(tasks, task_id)
    return result



def main(file_path="tasks.json"):
    tasks = load_tasks(file_path)

    while True:
        print("===== TASK MANAGER ====")

        choice = input("Choose an option.")

        if choice == "1":
            add_task_cli(tasks)
            save_tasks(tasks, file_path)
        elif choice == "2":
            list_tasks_cli(tasks)
        elif choice == "3":
            result = complete_task_cli(tasks)
            if result == "completed":
                save_tasks(tasks, file_path)
        elif choice == "4":
            result = delete_task_cli(tasks)
            if result == "deleted":
                save_tasks(tasks, file_path)
        elif choice == "5":
            result = update_task_cli(tasks)
            if result is not None:
                save_tasks(tasks, file_path)
        elif choice == "6":
            print("Goodbye")
            break

    




if __name__ == "__main__":
    main()