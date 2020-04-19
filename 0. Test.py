import turtle, tkinter

def dog_draw_square():
    t=turtle.Pen()
    for x in range(1,5):
        t.forward(50)
        t.left(90)
    print("Dog has done its' job drawing")

tk=tkinter.Tk()
btn=tkinter.Button(tk,text="Click to Draw", command=dog_draw_square)
btn.pack()

tk.mainloop()
