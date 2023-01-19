import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from model import TextModel
from view import TextView


# This class represents a Controller for the GUI elements
class TextController:
    def __init__(self, root):
        self.model = TextModel()
        self.view = TextView(root)

        self.view.search_button.config(command=self.search)
        self.view.load_button.config(command=self.load)
        self.view.pattern_entry.bind("<Return>", lambda _event: self.search())

    # Load text into model property and GUI's Text Area
    def load_text(self, text):
        self.model.set_text(text)
        self.view.set_text(text)

    # Search for a certain pattern and finally highlight it when found
    def search(self):
        # Check if Text is a placeholder
        if str(self.view.text.get("1.0", 'end-1c')) == TextView.placeholder:
            return

        # Check if pattern isn't empty
        pattern = self.view.pattern_entry.get()
        if len(pattern) == 0:
            return

        # Check if pattern doesn't end with escape sign
        if pattern[-1] == "\\":
            messagebox.showerror("Error", "Pattern cannot end with \"escape sign\" (backslash)")
            return
        
        text = self.view.text.get("1.0", tk.END)

        # Handling case sensitive checkbox
        case_sensitive = self.view.case_sensitive_var.get()
        if not case_sensitive:
            text = text.lower()
            pattern = pattern.lower()

        self.model.set_text(text)
        self.model.set_pattern(pattern)
        
        self.model.search()
        occurrences = self.model.get_occurrences()

        self.view.highlight_pattern(occurrences, len(pattern))
        self.view.set_occurrences(len(occurrences))

    # Load text from file
    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # Check if user selected any file
        if not filename:
            return

        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            self.load_text(text)
