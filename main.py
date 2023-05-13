import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    chars = ''
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length)) if chars else ''

def on_generate_click():
    password_length = int(spinbox.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    generated_password = generate_password(password_length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    password.set(generated_password)

def on_copy_click():
    root.clipboard_clear()
    root.clipboard_append(password.get())

root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("400x300")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="Password Length:").grid(column=0, row=0, sticky=tk.W)
spinbox = ttk.Spinbox(main_frame, from_=4, to=32, width=5)
spinbox.grid(column=1, row=0, sticky=tk.W)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var).grid(column=0, row=1, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var).grid(column=1, row=1, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Numbers", variable=numbers_var).grid(column=0, row=2, sticky=tk.W)
ttk.Checkbutton(main_frame, text="Symbols", variable=symbols_var).grid(column=1, row=2, sticky=tk.W)

password = tk.StringVar()
ttk.Label(main_frame, text="Generated Password:").grid(column=0, row=3, sticky=tk.W)
password_label = ttk.Label(main_frame, textvariable=password)
password_label.grid(column=1, row=3, sticky=tk.W)

generate_button = ttk.Button(main_frame, text="Generate", command=on_generate_click)
generate_button.grid(column=0, row=4, columnspan=2)

copy_button = ttk.Button(main_frame, text="Copy", command=on_copy_click)
copy_button.grid(column=0, row=5, columnspan=2)

root.mainloop()
