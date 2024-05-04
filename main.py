from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translater")
root.geometry("500x800")
root.config(bg='red')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50, width=300)


frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), fg='Black', bg="Red")
lab_txt.place(x=100, y=100, height=20, width=300)

sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)



root.mainloop()