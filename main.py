import tkinter
from controller import TextController

root = tkinter.Tk()  # Initialize tkinter
app = TextController(root)  # Create an instance of the TextController
root.mainloop()  # Run graphical interface
