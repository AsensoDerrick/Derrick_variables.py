# To-Do List Application
# Author: Asenso Derrick
# Description: A simple To-Do List app that allows users to add, view, complete, and delete tasks.

# List to store tasks
tasks = []

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!\n")

# Function to display all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓ Completed" if task["completed"] else "✗ Pending"
            print(f"{i}. {task['task']} - {status}")
        print()

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Function to delete a task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

# Main program loop
def main():
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.\n")

# Run the application
if __name__ == "__main__":
    main()
