import tkinter
from controller import TextController

root = tkinter.Tk()  # Initiliazie tkinter
app = TextController(root)  # Create an instance of the TextController
root.mainloop()  # Run graphical interface
