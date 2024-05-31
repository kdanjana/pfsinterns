from tkinter import *
from tkinter import ttk
import string
import secrets
import pyperclip

def generator():
    password_len = int(length_Box.get())
    if password_len < 8 or password_len > 32:
        passwordField.delete(0, END)
        passwordField.insert(0, "Error: Password length should be between 8 and 32 characters.")
        return

    all_comb = []
    if uppercase_var.get():
        all_comb.extend(list(string.ascii_uppercase))
    if lowercase_var.get():
        all_comb.extend(list(string.ascii_lowercase))
    if digits_var.get():
        all_comb.extend((string.digits))
    if special_chars_var.get():
        all_comb.extend((string.punctuation))
    
    if not all_comb:
        passwordField.delete(0, END)
        passwordField.insert(0, "Error: Select at least one character set.")
        return
    
    comb = ''.join(all_comb)
    password = ''.join(secrets.choice(comb) for _ in range(password_len))
    passwordField.delete(0, END)
    passwordField.insert(0, password)


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)
    messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard!")

# Initialize the main window
root = Tk() 
root.geometry("400x400")
root.title("Password Generator")
Font = ('arial', 13, 'bold')

# Create a label to add a text
passwordlabel = Label(root, text='Password Generator', font=('Times', 18, 'bold'))
passwordlabel.grid(row=0, column=0, padx=10, pady=10)

# Length of password
lengthlabel = Label(root, text="Password Length (8-32)", font=('cairo', 13, 'bold'))
lengthlabel.grid(row=1, column=0)
length_Box = Spinbox(root, from_=8, to_=32, font=Font, width=5, wrap=True)
length_Box.grid(row=1, column=2, pady=20, padx=10)

# Checkboxes for character sets
uppercase_var = BooleanVar()
uppercase_check = ttk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=2, column=0, sticky=W, padx=10)

lowercase_var = BooleanVar()
lowercase_check = ttk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=3, column=0, sticky=W, padx=10)

digits_var = BooleanVar()
digits_check = ttk.Checkbutton(root, text="Digits (0-9)", variable=digits_var)
digits_check.grid(row=4, column=0, sticky=W, padx=10)

special_chars_var = BooleanVar()
special_chars_check = ttk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_check.grid(row=5, column=0, sticky=W, padx=10)

generateButton = Button(root, text='Generate', font=(Font, 10, 'bold'), command=generator)
generateButton.grid(row=6, column=0, pady=5)

passwordField = Entry(root, width=20, bd=2, font=Font)
passwordField.grid(row=6, column=2)

copyButton = Button(root, text='Copy to Clipboard', font=(Font, 10, 'bold'), command=copy)
copyButton.grid(row=7, column=0, pady=5, columnspan=3)

root.mainloop()
