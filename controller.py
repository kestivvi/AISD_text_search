import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from model import TextModel
from view import TextView

class TextController:
    def __init__(self, root):
        self.model = TextModel()
        self.view = TextView(root)

        self.view.search_button.config(command=self.search)
        self.view.load_button.config(command=self.load)
        self.view.pattern_entry.bind("<Return>", lambda event: self.search())

    def load_text(self, text):
        self.model.load_text(text)
        self.view.set_text(text)

    def search(self):
        pattern = self.view.pattern_entry.get()
        if len(pattern) == 0:
            return

        if pattern[-1] == "\\":
            messagebox.showerror("Błąd", "Wzorzec nie może konczyć się \"znakiem ucieczki\" (backslash)")
            return

        text = self.view.text.get("1.0", tk.END)
        self.model.load_text(text)
        self.model.set_pattern(pattern)
        self.model.search()
        self.view.highlight_pattern(pattern)
        self.view.set_occurrences(self.model.get_occurrences())
    
    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            self.load_text(text)
