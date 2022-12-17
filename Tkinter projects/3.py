from tkinter import *
# Window
root = Tk()

# Functions
def myclick():
	myLabel= Label(root, 
		text="Look! I clicked a Button!")
	myLabel.pack()

# Create
button_1 = Button(root, 
	text="Click me!",
	command=myclick,
	fg="#ffffff",
	bg="gray")

# Place
button_1.pack()


root.mainloop()
