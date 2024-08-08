import os

TODO_FILE = "todo_list.txt"

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

def remove_task(task_number):
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    
    if task_number < 1 or task_number > len(tasks):
        print(f"Invalid task number: {task_number}")
        return
    
    removed_task = tasks.pop(task_number - 1).strip()
    
    with open(TODO_FILE, "w") as file:
        file.writelines(tasks)
    
    print(f"Task '{removed_task}' removed from the to-do list.")

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task = input("Enter the task: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to remove: ").strip())
            remove_task(task_number)
        elif choice == "4":
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
