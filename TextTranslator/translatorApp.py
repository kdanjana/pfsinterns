from tkinter import *
import googletrans
from translate import Translator
from tkinter import ttk, messagebox



# List of languages from googletrans
languages = googletrans.LANGUAGES
languageList = list(languages.values())
languageLists = [lang.capitalize() for lang in languageList]

# Function to translate text
def translateText():
    translatedText.delete(1.0,END)
    fromLanguageKey = 'en'
    toLanguageKey = None
    try:
        # Get the input language key
        for key, value in languages.items():
            if value.capitalize() == inputBox.get():
                fromLanguageKey = key

        # Get the translated language key
        for key, value in languages.items():
            if value.capitalize() == translatedBox.get():
                toLanguageKey = key

        if fromLanguageKey and toLanguageKey:
            # Translate input text
            translator = Translator(from_lang=inputBox.get(), to_lang=translatedBox.get())
            translatedWords = translator.translate(inputText.get(1.0, END))
            translatedText.insert(1.0, translatedWords)
        else:
            raise ValueError("Invalid language selection.")
    except Exception as e:
        messagebox.showerror("Translator", str(e))

# Function to clear text boxes
def clearText():
    inputText.delete(1.0, END)
    translatedText.delete(1.0, END)
    inputBox.set('English') 
    translatedBox.set('Select language')

# Initialize the main window
root = Tk()
root.title('Text Translator')
root.geometry("800x300")

# Text box for input
inputText = Text(root, height=10, width=40)
inputText.grid(row=0, column=0, pady=20, padx=10)

# Button to trigger translation
translateButton = Button(root, text="Translate", command=translateText)
translateButton.grid(row=0, column=1, padx=10)

# Text box for translated output
translatedText = Text(root, height=10, width=40)
translatedText.grid(row=0, column=2, pady=20, padx=10)

# Combobox for input text language selection
inputBox = ttk.Combobox(root, width=40, font=('Arial', 9, 'bold'), value=languageLists)
inputBox.set('English')  # Default input text language is English
inputBox.grid(row=1, column=0)

# Combobox for translated text language selection
translatedBox = ttk.Combobox(root, width=40, font=('Arial', 9, 'bold'), value=languageLists)
translatedBox.set('Select language')
translatedBox.grid(row=1, column=2)

# Clear button
clearButton = Button(root, text="Clear", command=clearText)
clearButton.grid(row=2, column=1)

# Start the Tkinter event loop
root.mainloop()
