from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame Demo")


frame = Frame(root, bg='white',padx=5,pady=5)


image1 = ImageTk.PhotoImage(Image.open("image1.jpg"))

image1_label= Label(frame, image=image1).grid(row=0,column=0)

image2 = ImageTk.PhotoImage(Image.open("image2.jpg"))

image2_label= Label(frame, image=image2).grid(row=0,column=1)

image3 = ImageTk.PhotoImage(Image.open("image3.jpg"))

image3_label= Label(frame, image=image3).grid(row=1,column=0)


frame.pack()

root.mainloop()

 