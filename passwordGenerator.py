#This is a simple application of password generator

import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, strength):
    characters = {
        'weak': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'strong': string.ascii_letters + string.digits + string.punctuation
    }
    password = ''.join(random.choice(characters[strength]) for i in range(length))
    return password

def copy_to_clipboard():
    result = result_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
    except ValueError as e:
        messagebox.showerror("Error", "Invalid input. Please enter a positive integer for the length.")
        return

    strength = strength_var.get()
    password = generate_password(length, strength)
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size and position it in the center of the screen
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create widgets with improved styling
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")
result_font = ("Arial", 14)

length_label = tk.Label(root, text="Enter the length of the password:", font=label_font)
length_label.pack()

length_entry = tk.Entry(root, font=entry_font)
length_entry.pack()

strength_label = tk.Label(root, text="Select the strength of the password:", font=label_font)
strength_label.pack()

strength_var = tk.StringVar()
strength_frame = tk.Frame(root)
strength_frame.pack()

weak_button = tk.Radiobutton(strength_frame, text="Weak", variable=strength_var, value="weak", font=label_font)
weak_button.pack(side=tk.LEFT)

medium_button = tk.Radiobutton(strength_frame, text="Medium", variable=strength_var, value="medium", font=label_font)
medium_button.pack(side=tk.LEFT)

strong_button = tk.Radiobutton(strength_frame, text="Strong", variable=strength_var, value="strong", font=label_font)
strong_button.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="Generate Password", command=generate, font=button_font, bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=button_font, bg="#008CBA", fg="white")
copy_button.pack(pady=5)

result_label = tk.Label(root, text="", font=result_font)
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
