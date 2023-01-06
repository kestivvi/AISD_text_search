import tkinter as tk

class TextView:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Search")

        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack()
        self.text = tk.Text(self.text_frame, width=100, height=30)
        self.text.pack()
        
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()
        
        self.load_button = tk.Button(self.control_frame, text="Load text from file")
        self.load_button.pack(side=tk.LEFT)
        
        self.pattern_label = tk.Label(self.control_frame, text="Pattern:")
        self.pattern_label.pack(side=tk.LEFT)
        
        self.pattern_entry = tk.Entry(self.control_frame)
        self.pattern_entry.pack(side=tk.LEFT)
        
        self.search_button = tk.Button(self.control_frame, text="Search")
        self.search_button.pack(side=tk.LEFT)
        
        self.occurrences_label = tk.Label(self.control_frame, text="Occurrences: 0")
        self.occurrences_label.pack(side=tk.LEFT)
        

    def set_text(self, text):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", text)

    def highlight_pattern(self, occurences, pattern_len):
        self.text.tag_remove("highlight", "1.0", tk.END)
        self.text.tag_config("highlight", background="yellow")
        
        start = "1.0"
        text = self.text.get("1.0", tk.END)

        for index in occurences:
            line = text.count("\n", 0, index) + 1
            column = index - text.rfind("\n", 0, index) - 1
            start = f"{line}.{column}"
            end = f"{start}+{pattern_len}c"
            self.text.tag_add("highlight", start, end)

    def set_occurrences(self, occurrences):
        self.occurrences_label.config(text=f"Occurrences: {occurrences}")
