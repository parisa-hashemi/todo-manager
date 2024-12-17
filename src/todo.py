tasks = []

def add_task(task_name, due_date):
    task = {"name": task_name, "due_date": due_date, "done": False}
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def edit_task(index, new_name, new_due_date):
    tasks[index]["name"] = new_name
    tasks[index]["due_date"] = new_due_date

def mark_done(index):
    tasks[index]["done"] = True

def delete_task(index):
    tasks.pop(index)


def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (e.g., 2024-12-20): ")
            add_task(task_name, due_date)
            print("Task added!")
        
        elif choice == "2":
            print("Your tasks:")
            tasks_list = list_tasks()
            for i, task in enumerate(tasks_list):
                print(f"{i+1}. {task['name']} - Due: {task['due_date']} - Done: {task['done']}")
        
        elif choice == "3":
            index = int(input("Enter task number to edit: ")) - 1
            if 0 <= index < len(tasks):
                new_name = input("Enter new task name: ")
                new_due_date = input("Enter new due date: ")
                edit_task(index, new_name, new_due_date)
                print("Task updated!")
            else:
                print("Invalid task number!")
        
        elif choice == "4":
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                mark_done(index)
                print("Task marked as done!")
            else:
                print("Invalid task number!")
        
        elif choice == "5":
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                delete_task(index)
                print("Task deleted!")
            else:
                print("Invalid task number!")
        
        elif choice == "6":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
