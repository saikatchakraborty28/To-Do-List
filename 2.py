from tkinter import *
from tkinter import ttk, messagebox

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry('650x410+300+150')

        # Main title label
        self.label = Label(self.root, text='TO-DO List App', font='Arial 25 bold', width=15, bd=5, bg='orange', fg='white')
        self.label.pack(side='top', fill=BOTH)

        # Label for adding tasks
        self.label2 = Label(self.root, text='Add Task', font='Arial 18 bold', width=10, bd=5, bg='green', fg='yellow')
        self.label2.place(x=10, y=50)

        # Label for displaying tasks
        self.label3 = Label(self.root, text='Tasks', font='Arial 18 bold', width=10, bd=5, bg='green', fg='yellow')
        self.label3.place(x=340, y=60)

        # Listbox to display tasks
        self.main_text = Listbox(self.root, height=12, bd=5, width=23, font="Arial 20 italic bold")
        self.main_text.place(x=200, y=100)
        
        # Textbox for inputting new tasks
        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial 10 bold')
        self.text.place(x=20, y=120)

        # Function to add a task
        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)  # Add task to the listbox
                with open('data.txt', 'a') as file:  # Save task to the file
                    file.write(content + '\n')
                self.text.delete(1.0, END)  # Clear the textbox
                messagebox.showinfo("Task Added", "Task added successfully!")  # Show success message
            else:
                messagebox.showwarning("No Task", "Please enter a task.")  # Show warning if textbox is empty

        # Function to delete a task
        def delete():
            selected_task_index = self.main_text.curselection()  # Get selected task index
            if selected_task_index:
                confirmation = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
                if confirmation:
                    selected_task = self.main_text.get(selected_task_index)  # Get selected task
                    self.main_text.delete(selected_task_index)  # Remove task from listbox

                    # Remove task from file
                    with open('data.txt', 'r') as file:
                        lines = file.readlines()
                    with open('data.txt', 'w') as file:
                        for line in lines:
                            if line.strip("\n") != selected_task:
                                file.write(line)
                    messagebox.showinfo("Task Deleted", "Task deleted successfully!")  # Show success message
            else:
                messagebox.showwarning("No Selection", "Please select a task to delete.")  # Show warning if no task selected

        # Load tasks from file into the listbox
        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            with open('data.txt', 'w') as file:
                pass  # Create the file if it doesn't exist

        # Button to add a task
        self.add_btn = Button(self.root, text='Add Task', font='Arial 14 bold', width=10, bd=5, bg='blue', fg='white', command=add)
        self.add_btn.place(x=30, y=160)

        # Button to delete a task
        self.del_btn = Button(self.root, text='Delete Task', font='Arial 14 bold', width=10, bd=5, bg='red', fg='white', command=delete)
        self.del_btn.place(x=30, y=210)

def main():
    root = Tk()
    ul = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
