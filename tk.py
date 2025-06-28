import tkinter as tk

root = tk.Tk()

# ======================= FUNCTIONS =======================
def add_task():
    task = entry.get()
    if task.strip():
        listbox.insert(tk.END, task.strip())
        entry.delete(0, tk.END)
        renumber_tasks()
    else:
        listbox.insert(tk.END, "Please enter a task.")

def delete_task():
    listbox.delete(tk.ANCHOR)
    renumber_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            listbox.delete(0, tk.END)
            for task in tasks:
                task = task.strip()
                if task:
                    listbox.insert(tk.END, task)
            renumber_tasks()
    except FileNotFoundError:
        pass

def renumber_tasks():
    tasks = listbox.get(0, tk.END)
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        if ". " in task:
            task = task.split(". ", 1)[-1]
        listbox.insert(tk.END, f"{i}. {task}")

# ======================= GUI SETUP =======================
root.title("To Do List")
root.resizable(True, True)
root.geometry("600x400")
root.minsize(600, 400)
root.maxsize(800, 600)
root.configure(bg="#e6f2ff")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Entry Field
entry = tk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")
entry.bind("<Return>", lambda event: add_task())

# Add Button
entry_button = tk.Button(frame, text="Add", command=add_task)
entry_button.grid(row=0, column=1, padx=5, pady=5)

# Listbox
listbox = tk.Listbox(frame, width=100, height=20, selectmode=tk.SINGLE)
listbox.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Save & Load Buttons
save_button = tk.Button(frame, text="Save", command=save_tasks)
save_button.grid(row=2, column=0, pady=5, sticky="w")

load_button = tk.Button(frame, text="Load", command=load_tasks)
load_button.grid(row=2, column=1, pady=5, sticky="e")

# ======================= BINDINGS =======================
listbox.bind("<Delete>", lambda e: delete_task())
listbox.bind("<Double-Button-1>", lambda e: delete_task())
listbox.bind("<Return>", lambda e: delete_task())
listbox.bind("<Button-3>", lambda e: delete_task())
listbox.bind("<Button-2>", lambda e: delete_task())
listbox.bind("<Button-1>", lambda e: listbox.selection_set(listbox.nearest(e.y)))
listbox.bind("<FocusIn>", lambda e: listbox.selection_set(0))
listbox.bind("<FocusOut>", lambda e: listbox.selection_clear(0))
listbox.bind("<MouseWheel>", lambda e: listbox.yview_scroll(int(-1*(e.delta/120)), "units"))
listbox.bind("<Button-4>", lambda e: listbox.yview_scroll(-1, "units"))
listbox.bind("<Button-5>", lambda e: listbox.yview_scroll(1, "units"))
#=======================BG COLOR CHANGE=======================
# Background color hex code
BG_COLOR = "#e6f2ff"  # Light blue

# Inside your GUI setup section
root.configure(bg=BG_COLOR)
frame.configure(bg=BG_COLOR)
entry.configure(bg="white", fg="black", insertbackground="black")  # Text color and cursor
listbox.configure(bg="white", fg="black")
# ======================= KEYBOARD SHORTCUTS =======================
root.bind("<Control-n>", lambda e: add_task())
root.bind("<Control-s>", lambda e: save_tasks())    

# ======================= STARTUP =======================
load_tasks()
root.mainloop()



