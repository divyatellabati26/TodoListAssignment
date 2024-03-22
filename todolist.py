# Function to display the current to-do list
def display_todo_list(todo_list):
    print("Current To-Do List:")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. [{task['status']}] {task['name']}")

# Function to add a task to the to-do list
def add_task(todo_list):
    task_name = input("Enter the task name: ")
    todo_list.append({"name": task_name, "status": "Incomplete"})
    print("Task added successfully!")

# Function to mark a task as completed
def mark_task_completed(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number you want to mark as completed: ")) - 1
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]['status'] = 'Completed'
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to remove a task from the to-do list
def remove_task(todo_list):
    display_todo_list(todo_list)
    task_number = int(input("Enter the task number you want to remove: ")) - 1
    if 0 <= task_number < len(todo_list):
        del todo_list[task_number]
        print("Task removed successfully!")
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []
    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
