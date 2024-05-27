#PIP INSTALL PILLOW


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("My Crypto Banking App")

root.configure( background="white")

image_logo = ImageTk.PhotoImage(Image.open("logo.jpeg"))
image_label= Label(root, image=image_logo)
image_label.pack(side="top")

frame = Frame(root, bg='white',padx=5,pady=5)

Label(frame,text="Account Number 1:",fg='black',bg='white').grid(row=0,column=0, sticky=W, pady=10)

Label(frame,text="Account Number 2:",fg='black',bg='white').grid(row=1, column=0, sticky=W, pady=10)

Label(frame,text="Private Key:",fg='black',bg='white').grid(row=2, column=0, sticky=W, pady=10)

Label(frame,text="ETH:",fg='black',bg='white').grid(row=3, column=0, sticky=W, pady=10)

Label(frame,text="Gas Price (GWEI):",fg='black',bg='white').grid(row=4, column=0, sticky=W, pady=10)

Label(frame,text="Gas Limit (GWEI):",fg='black',bg='white').grid(row=5, column=0, sticky=W, pady=10)


frame.pack()

root.mainloop()




