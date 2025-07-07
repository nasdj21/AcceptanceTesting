from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_task_by_hand(self, description, due_date=None, priority=None):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            return "No tasks found."
        output = ["Tasks:"]
        for i, task in enumerate(self.tasks, start = 1):
            status = "Completed" if task.completed else "Pending"
            output.append(f"{i}. {task.description} [Status: {status}]")
        return "\n".join(output)
    
    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                return True
            return False
    
    def clear_tasks(self):
        self.tasks.clear()


if __name__ == "__main__":
    import sys
    todo = ToDoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Clear Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)
            print("Task added.")
        elif choice == "2":
            print(todo.list_tasks())
        elif choice == "3":
            desc = input("Enter task to complete: ")
            if todo.complete_task(desc):
                print("Task marked as completed.")
            else:
                print("Task not found.")
        elif choice == "4":
            todo.clear_tasks()
            print("All tasks cleared.")
        elif choice == "5":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid option.")
