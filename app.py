# Simple To-Do List Application

def display_tasks(tasks):
    """Display all tasks in the to-do list."""
    if not tasks:
        print("\nNo tasks in the list. Add some!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"'{removed_task}' has been removed from the list.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    """Main function to run the to-do list application."""
    tasks = []
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
