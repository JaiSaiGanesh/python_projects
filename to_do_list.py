from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.history = []
        self.future = []

    def add_task(self, task, due_date=None):
        task_info = {"task": task, "due_date": due_date}
        self.tasks.append(task_info)
        self.history.append(("add", task_info))
        self.future = []  # Clear redo history
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.history.append(("remove", removed_task))
            self.future = []  # Clear redo history
            print(f"Task '{removed_task['task']}' removed from the to-do list.")
        else:
            print("Invalid task index.")

    def undo(self):
        if self.history:
            action, task_info = self.history.pop()
            if action == "add":
                self.tasks.remove(task_info)
            elif action == "remove":
                self.tasks.insert(0, task_info)  # Insert at the beginning for accurate task index
            self.future.append((action, task_info))
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.future:
            action, task_info = self.future.pop()
            if action == "add":
                self.tasks.append(task_info)
            elif action == "remove":
                self.tasks.remove(task_info)
            self.history.append((action, task_info))
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    def show_tasks(self):
        if self.tasks:
            print("Tasks in the to-do list:")
            for index, task_info in enumerate(self.tasks, start=1):
                task = task_info["task"]
                due_date = task_info["due_date"]
                due_date_str = f" (Due: {due_date})" if due_date else ""
                print(f"{index}. {task}{due_date_str}")
        else:
            print("No tasks in the to-do list.")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Undo")
        print("5. Redo")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(task, due_date)
        elif choice == "2":
            todo_list.show_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            todo_list.undo()
        elif choice == "5":
            todo_list.redo()
        elif choice == "6":
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()





