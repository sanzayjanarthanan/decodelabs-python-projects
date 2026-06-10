import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"id": len(tasks) + 1, "task": task})
        save_tasks(tasks)
        print(f"✅ Task added!")
    else:
        print("Empty task skipped.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for i, item in enumerate(tasks, start=1):
        print(f"{i}. {item['task']}")
    print()

def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()