# main.py
from tasks_operations import add_task, remove_task, list_tasks
from tasks_storage import save_tasks, load_tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nHello kamal,  Welcome to To-Do List Application ")
        print(" 1. Add Task")
        print(" 2. Remove Task")
        print(" 3. List Tasks")
        print(" 4. Mark Task as Completed")
        print(" 5. Exit")
        choice = input("Choose an option: ")

        #making user to choose among 5 choices to do different function
        if choice == "1":
            title = input("Enter task title: ")
            add_task(tasks, title)
            save_tasks(tasks)
            print(f"Task '{title}' added successfully.")
        elif choice == "2":
            title = input("Enter task title to remove: ")
            if remove_task(tasks, title):
                save_tasks(tasks)
                print(f"Task '{title}' removed successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            print("\n=== Task List ===")
            for task in list_tasks(tasks):
                status = "[done]" if task["completed"] else "[ ]"
                print(f"{status} {task['title']}")
        elif choice == "4":
            title = input("Enter task title to mark as completed: ")
            for task in tasks:
                if task.title == title:
                    task.completed = True
                    save_tasks(tasks)
                    print(f"Task '{title}' marked as completed.")
                    break
            else:  #if there is no such task
                print("Task not found.")
        elif choice == "5":
            print("Exiting... Thank you,  have a good day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
