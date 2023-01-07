import tkinter as tk


# This class represents a GUI styling
class TextView:
    # Default placeholder text
    placeholder = "Type some text.."

    # Default background color
    background_color = "#F5F5F5";

    def __init__(self, root, check_length=None):
        self.root = root
        self.root.geometry("800x480")
        self.root.configure(bg='white')
        self.root.title("Text Search ;)")

        # Sentence label
        self.info_label = tk.Label(self.root, text="Please specify a sentence:", background="white", width=95,
                                   font=("Calibri", 11), anchor="w")
        self.info_label.pack(padx=8, pady=6,
                             anchor="w")  # In this case, anchor="w" is responsible for text align: left

        # Text entry
        self.text = tk.Text(self.root, width=95, height=20, borderwidth=1, relief="solid")
        self.text.pack()
        self.text.insert('1.0', self.placeholder)
        self.text.bind("<FocusIn>", self.clear_placeholder)
        self.text.bind("<FocusOut>", self.put_placeholder)

        # Bottom control panel
        self.control_frame = tk.Frame(self.root, background=self.background_color)
        self.control_frame.pack(pady=40)

        # Load text from file button
        self.load_button = tk.Button(self.control_frame, text="Load text from file")
        self.load_button.pack(side=tk.LEFT, padx=15)

        # Label for an input
        self.pattern_label = tk.Label(self.control_frame, text="Pattern:", background=self.background_color)
        self.pattern_label.pack(side=tk.LEFT)

        # Input for a pattern that we search for
        self.pattern_entry = tk.Entry(self.control_frame)
        self.pattern_entry.pack(side=tk.LEFT)

        # Search pattern in text button
        self.search_button = tk.Button(self.control_frame, text="Search")
        self.search_button.pack(side=tk.LEFT, padx=3)

        # Label informing about occurrences count
        self.occurrences_label = tk.Label(self.control_frame, text="Occurrences: 0", background=self.background_color)
        self.occurrences_label.pack(side=tk.LEFT, padx=15)

    # Clear a placeholder from Text Area on click
    def clear_placeholder(self, event):
        if self.text.get("1.0", 'end-1c') == TextView.placeholder:
            self.text.delete("1.0", 'end')

    # Insert a placeholder for Text Area when it's empty
    def put_placeholder(self, event):
        if len(self.text.get("1.0", 'end-1c')) == 0:
            self.text.insert("1.0", TextView.placeholder)

    # Clear Text Area and insert text from parameter
    def set_text(self, text):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", text)

    # Highlight all occurrences of searched pattern
    def highlight_pattern(self, occurrences, pattern_len):
        self.text.tag_remove("highlight", "1.0", tk.END)
        self.text.tag_config("highlight", background="yellow")

        start = "1.0"
        text = self.text.get("1.0", tk.END)

        # "occurrences" stores count of found pattern
        for index in occurrences:
            line = text.count("\n", 0, index) + 1
            column = index - text.rfind("\n", 0, index) - 1
            start = f"{line}.{column}"
            end = f"{start}+{pattern_len}c"
            self.text.tag_add("highlight", start, end)

    # Update occurrences count
    def set_occurrences(self, occurrences):
        self.occurrences_label.config(text=f"Occurrences: {occurrences}")
