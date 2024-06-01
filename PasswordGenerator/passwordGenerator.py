from tkinter import *
from tkinter import ttk, messagebox
import string
import secrets
import pyperclip

def generator():
    passwordLen = int(lengthBox.get())
    print(passwordLen)
    if passwordLen < 8 or passwordLen > 32:
        passwordField.delete(0, END)
        messagebox.showinfo( "Error: Password length should be between 8 and 32 characters.")
        return

    allComb = []
    if uppercaseVar.get():
        allComb.extend(list(string.ascii_uppercase))
    if lowercaseVar.get():
        allComb.extend(list(string.ascii_lowercase))
    if digitsVar.get():
        allComb.extend((string.digits))
    if specialCharsVar.get():
        allComb.extend((string.punctuation))
    
    if not allComb:
        passwordField.delete(0, END)
        messagebox.showinfo( "Error", " Select at least one character set.")
        return
    
    comb = ''.join(allComb)
    password = ''.join(secrets.choice(comb) for _ in range(passwordLen))
    passwordField.delete(0, END)
    passwordField.insert(0, password)


def copy():
    randomPassword = passwordField.get()
    pyperclip.copy(randomPassword)
    messagebox.showinfo("Copy to Clipboard", "Password copied to clipboard!")


def clear():
    passwordField.delete(0, END)
    uppercaseVar.set(False)
    lowercaseVar.set(False)
    digitsVar.set(False)
    specialCharsVar.set(False)
    defaultValue = 8
    lengthBox.delete(0,END)
    lengthBox.insert(0,defaultValue)



# Initialize the main window
root = Tk() 
root.geometry("400x400")
root.title("Password Generator")
Font = ('arial', 13, 'bold')

# Create a label to add a text
passwordLabel = Label(root, text='Password Generator', font=('Times', 18, 'bold'))
passwordLabel.grid(row=0, column=0, padx=10, pady=10)

# Length of password
lengthLabel = Label(root, text="Password Length (8-32)", font=('cairo', 13, 'bold'))
lengthLabel.grid(row=1, column=0)
lengthBox = Spinbox(root, from_=8, to_=32, font=Font, width=6, wrap=True)
lengthBox.grid(row=1, column=1, pady=20, padx=10)

# Checkboxes for character sets
uppercaseVar = BooleanVar()
uppercaseCheck = ttk.Checkbutton(root, text="Uppercase Letters", variable=uppercaseVar)
uppercaseCheck.grid(row=2, column=0, sticky=W, padx=50, pady=5)

lowercaseVar = BooleanVar()
lowercaseCheck = ttk.Checkbutton(root, text="Lowercase Letters", variable=lowercaseVar)
lowercaseCheck.grid(row=3, column=0, sticky=W,  padx=50, pady=5)

digitsVar = BooleanVar()
digitsCheck = ttk.Checkbutton(root, text="Digits (0-9)", variable=digitsVar)
digitsCheck.grid(row=4, column=0, sticky=W, padx=50, pady=5)

specialCharsVar = BooleanVar()
specialCharsCheck = ttk.Checkbutton(root, text="Special Characters", variable=specialCharsVar)
specialCharsCheck.grid(row=5, column=0, sticky=W,  padx=50, pady=5)

generateButton = Button(root, text='Generate', font=(Font, 10, 'bold'), command=generator, width=20)
generateButton.grid(row=6, column=0, pady=5, padx=50)

passwordField = Entry(root, width=20, bd=2, font=Font)
passwordField.grid(row=7, column=0, pady=5, padx=50)

copyButton = Button(root, text='Copy to Clipboard', font=(Font, 10, 'bold'), command=copy)
copyButton.grid(row=8, column=0, pady=5, columnspan=1)

copyButton = Button(root, text='Clear', font=(Font, 10, 'bold'), command=clear)
copyButton.grid(row=9, column=0, pady=5)

root.mainloop()
