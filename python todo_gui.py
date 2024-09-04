import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append({"name": task_name, "completed": False})
    save_tasks(tasks)

def view_tasks(tasks):
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - {status}")

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        task_name = input("Enter the new task name: ")
        tasks[task_num]["name"] = task_name
        save_tasks(tasks)

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        save_tasks(tasks)

def mark_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_completed(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()
        
        self.task_listbox = tk.Listbox(root, height=10, width=50)
        self.task_listbox.pack(pady=10)
        self.update_task_listbox()
        
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
    
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " (Completed)" if task["completed"] else ""
            self.task_listbox.insert(tk.END, task["name"] + status)
    
    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.tasks.append({"name": task_name, "completed": False})
            self.save_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task name cannot be empty.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.save_tasks()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
