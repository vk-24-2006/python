import tkinter as tk
from tkinter import messagebox

FILE_NAME = "goals.txt"

def save_goal():
    goal = goal_entry.get()
    milestone = milestone_entry.get()
    if goal == "" or milestone == "":
        messagebox.showwarning("Warning", "Please enter both goal and milestone")
        return

    with open(FILE_NAME, "a") as f:
        f.write(f"Goal: {goal} | Milestone: {milestone}\n")

    goal_entry.delete(0, tk.END)
    milestone_entry.delete(0, tk.END)
    load_goals()
    messagebox.showinfo("Saved", "Goal and milestone saved successfully!")


def load_goals():
    listbox.delete(0, tk.END)
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        open(FILE_NAME, "w").close()  

def delete_goal():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a goal to delete")
        return

    index = selected[0]
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for i, line in enumerate(lines):
            if i != index:
                f.write(line)
    load_goals()
    messagebox.showinfo("Deleted", "Goal deleted successfully!")


root = tk.Tk()
root.title("Simple Goal Planner")
root.geometry("500x400")

tk.Label(root, text="Goal Planner", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter Long-term Goal:").pack()
goal_entry = tk.Entry(root, width=50)
goal_entry.pack(pady=5)

tk.Label(root, text="Enter Milestone:").pack()
milestone_entry = tk.Entry(root, width=50)
milestone_entry.pack(pady=5)

tk.Button(root, text="Save Goal", width=15, command=save_goal).pack(pady=5)
tk.Button(root, text="Delete Selected Goal", width=20, command=delete_goal).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)


load_goals()

root.mainloop()
