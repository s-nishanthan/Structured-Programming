# To-Do List - Structured Programming Example

# Function to display the to-do list
def display_list(to_do_list):
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(to_do_list, task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task from the list
def remove_task(to_do_list, task_number):
    if 0 < task_number <= len(to_do_list):
        removed_task = to_do_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task number.")

# Main function to interact with the to-do list
def main():
    to_do_list = []
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4): ")
        
        if choice == '1':
            display_list(to_do_list)
        elif choice == '2':
            task = input("Enter the task you want to add: ")
            add_task(to_do_list, task)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(to_do_list, task_number)
        elif choice == '4':
            print("Exiting the To-Do List app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
