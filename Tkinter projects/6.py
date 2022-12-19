from tkinter import *
from PIL import ImageTk,Image

main = Tk()
main.title("Dave :D")
main.iconbitmap("asset/user.ico")

img_1 = ImageTk.PhotoImage(Image.open("asset/Screenshot_20221203_122450_Antimatter Dimensions.png"))

my_label = Label(image=img_1)

my_label.pack()

main.mainloop()
