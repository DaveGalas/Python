from tkinter import *

main = Tk()
main.title("Simple Calculator")

# Variables
button_width = 5
button_height = 3


# Functions
def button_click(n):
    current = entry_1.get()
    entry_1.delete(0, END)
    entry_1.insert(0, str(current) + str(n))


def button_clear():
    entry_1.delete(0, END)

def button_add():



# Create widgets

entry_1 = Entry(main, width=30)

button_1 = Button(main, text="1", width=button_width, height=button_height, command=lambda: button_click(1))
button_2 = Button(main, text="2", width=button_width, height=button_height, command=lambda: button_click(2))
button_3 = Button(main, text="3", width=button_width, height=button_height, command=lambda: button_click(3))
button_4 = Button(main, text="4", width=button_width, height=button_height, command=lambda: button_click(4))
button_5 = Button(main, text="5", width=button_width, height=button_height, command=lambda: button_click(5))
button_6 = Button(main, text="6", width=button_width, height=button_height, command=lambda: button_click(6))
button_7 = Button(main, text="7", width=button_width, height=button_height, command=lambda: button_click(7))
button_8 = Button(main, text="8", width=button_width, height=button_height, command=lambda: button_click(8))
button_9 = Button(main, text="9", width=button_width, height=button_height, command=lambda: button_click(9))
button_0 = Button(main, text="0", width=button_width, height=button_height, command=lambda: button_click(0))

button_add = Button(main, text="+", width=button_width, height=button_height, command=lambda: button_add("+"))
button_equal = Button(main, text="=", width=button_width, height=button_height, command=lambda: button_clear("equal"))
button_clear = Button(main, text="CE", width=button_width, height=button_height, command=button_clear)

# Stuff them in

entry_1.grid(row=1, column=0, columnspan=5)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)

button_add.grid(row=2, column=4)
button_equal.grid(row=5, column=4)
button_clear.grid(row=5, column=2)

main.mainloop()
