def display_menu():
    print("\n=== To-Do List Menu ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")


def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_number - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
