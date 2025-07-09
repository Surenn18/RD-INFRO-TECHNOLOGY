import json
import os

TASKS_FILE = 'tasks.json'

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {'title': self.title, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['title'], data['completed'])

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        data = json.load(file)
        return [Task.from_dict(task) for task in data]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task.completed else "✘"
        print(f"{idx}. [{status}] {task.title}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append(Task(title))
        print("Task added.")
    else:
        print("Task title cannot be empty.")

def complete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task: {deleted.title}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
