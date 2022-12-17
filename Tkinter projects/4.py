from tkinter import *
# Window
root = Tk()

# Variables
name = ""

# Functions
def onclick():
	label_2 = Label(root, text=entry_1.get())
	label_2.grid(row=1, column=0)

# Create
label_1 = Label(root,
	text = "Name: ")
entry_1 = Entry(root,
	width = 30)
button_1 = Button(root,
	text = "Submit",
	command = onclick)

# Place
label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=0, column=2)

root.mainloop()
