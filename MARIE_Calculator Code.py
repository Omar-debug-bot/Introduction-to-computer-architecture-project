import math
import tkinter as tk
from tkinter import messagebox

# MARIE Registers
AC = 0
PC = 0
IR = 0
memory = {}

def load(value):
    global AC
    memory[100] = value
    AC = memory[100]

def store():
    memory[102] = AC
    return memory[102]

def update_registers():
    reg_label.config(text=f"AC = {round(AC, 6)}    PC = {PC}    IR = {IR}")

def calculate(op):
    global AC, PC, IR, memory

    try:
        if op in ['ADD', 'SUBT', 'MULTIPLY', 'DIVIDE', 'POWER']:
            a = float(entry1.get())
            b = float(entry2.get())
            load(a)
            memory[101] = b

            if op == 'ADD':
                AC += memory[101]
                IR = 'ADD'
            elif op == 'SUBT':
                AC -= memory[101]
                IR = 'SUBT'
            elif op == 'MULTIPLY':
                AC *= memory[101]
                IR = 'MULTIPLY'
            elif op == 'DIVIDE':
                if b == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                AC /= memory[101]
                IR = 'DIVIDE'
            elif op == 'POWER':
                AC = AC ** memory[101]
                IR = 'POWER'

        else:
            a = float(entry1.get())
            load(a)

            if op == 'SQRT':
                if a < 0:
                    messagebox.showerror("Error", "Cannot sqrt negative number")
                    return
                AC = math.sqrt(AC)
                IR = 'SQRT'
            elif op == 'SIN':
                AC = math.sin(math.radians(AC))
                IR = 'SIN'
            elif op == 'COS':
                AC = math.cos(math.radians(AC))
                IR = 'COS'
            elif op == 'TAN':
                AC = math.tan(math.radians(AC))
                IR = 'TAN'
            elif op == 'LOG':
                if a <= 0:
                    messagebox.showerror("Error", "Log only works on positive numbers")
                    return
                AC = math.log10(AC)
                IR = 'LOG10'
            elif op == 'LN':
                if a <= 0:
                    messagebox.showerror("Error", "Ln only works on positive numbers")
                    return
                AC = math.log(AC)
                IR = 'LN'
            elif op == 'FACT':
                AC = math.factorial(int(AC))
                IR = 'FACTORIAL'
            elif op == 'ABS':
                AC = abs(AC)
                IR = 'ABS'

        result = store()
        PC += 1
        result_label.config(text=f"Result = {round(result, 6)}")
        update_registers()

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def clear():
    global AC, PC, IR, memory
    AC = 0
    PC = 0
    IR = 0
    memory = {}
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result = ")
    update_registers()

# ── Main Window ──
root = tk.Tk()
root.title("MARIE Scientific Calculator")
root.geometry("500x620")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# ── Title ──
tk.Label(root, text="MARIE Scientific Calculator",
         font=("Arial", 16, "bold"),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=10)

# ── Input Fields ──
frame_inputs = tk.Frame(root, bg="#1e1e2e")
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="First Number:",
         bg="#1e1e2e", fg="#cdd6f4",
         font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(frame_inputs, font=("Arial", 11), width=15,
                  bg="#313244", fg="white", insertbackground="white")
entry1.grid(row=0, column=1, padx=10)

tk.Label(frame_inputs, text="Second Number:",
         bg="#1e1e2e", fg="#cdd6f4",
         font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(frame_inputs, font=("Arial", 11), width=15,
                  bg="#313244", fg="white", insertbackground="white")
entry2.grid(row=1, column=1, padx=10)

tk.Label(root, text="(Second number only needed for +  -  *  /  **)",
         bg="#1e1e2e", fg="#6c7086",
         font=("Arial", 9)).pack()

# ── Buttons ──
btn_style = {"font": ("Arial", 10, "bold"), "width": 8, "height": 2,
             "bd": 0, "cursor": "hand2"}

frame_btns = tk.Frame(root, bg="#1e1e2e")
frame_btns.pack(pady=10)

buttons = [
    ("+",     "ADD"),
    ("-",     "SUBT"),
    ("×",     "MULTIPLY"),
    ("÷",     "DIVIDE"),
    ("x^y",   "POWER"),
    ("√",     "SQRT"),
    ("sin",   "SIN"),
    ("cos",   "COS"),
    ("tan",   "TAN"),
    ("log",   "LOG"),
    ("ln",    "LN"),
    ("x!",    "FACT"),
    ("|x|",   "ABS"),
]

colors = ["#89b4fa", "#89dceb", "#a6e3a1", "#f38ba8", "#fab387"]

for i, (label, op) in enumerate(buttons):
    color = colors[i % len(colors)]
    btn = tk.Button(frame_btns, text=label,
                    bg=color, fg="#1e1e2e",
                    command=lambda o=op: calculate(o),
                    **btn_style)
    btn.grid(row=i // 5, column=i % 5, padx=5, pady=5)

# ── Result ──
result_label = tk.Label(root, text="Result = ",
                        font=("Arial", 14, "bold"),
                        bg="#1e1e2e", fg="#a6e3a1")
result_label.pack(pady=10)

# ── Registers Display ──
tk.Label(root, text="MARIE Registers:",
         bg="#1e1e2e", fg="#cdd6f4",
         font=("Arial", 11, "bold")).pack()

reg_label = tk.Label(root, text="AC = 0    PC = 0    IR = 0",
                     font=("Arial", 11),
                     bg="#313244", fg="#cdd6f4",
                     padx=10, pady=8)
reg_label.pack(pady=5, padx=20, fill="x")

# ── Clear Button ──
tk.Button(root, text="Clear / Reset",
          bg="#f38ba8", fg="#1e1e2e",
          font=("Arial", 11, "bold"),
          width=15, height=2, bd=0,
          cursor="hand2",
          command=clear).pack(pady=10)

root.mainloop()