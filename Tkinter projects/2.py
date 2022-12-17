from tkinter import *

root = Tk()

# Create
label_1 = Label(root, text="Hello World!")
label_2 = Label(root, text="How r u lmaoshahaha")
label_3 = Label(root, text="what the hell")


# Place
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=1)
label_3.grid(row=2, column=2)

root.mainloop()
