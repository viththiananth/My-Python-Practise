from tkinter import *

root=Tk()
Logo=PhotoImage(file="E:/1. Python/5. My Python Practice_VS Code/My-Python-Practise/tkinter/a3724efc0c85bd69c4366d96547cb667.gif")

right_label=Label(root,image=Logo)
right_label.pack(side="right")

left_label=(Label(root,justify=RIGHT,padx=10,text="This is Viththi")).pack(side="left")

print("Launching Window")
root.mainloop()