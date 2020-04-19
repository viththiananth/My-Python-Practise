import tkinter as tk

#Create Instance
parent=tk.Tk()
parent.title("-Welcome to Python tkinter Basic exercises-")
parent.geometry('600x300')
parent.resizable(0,0)

#Create Label
#my_label=tk.Label(parent,text="Label Widget",font=("Arial Bold",1))
#my_label.grid(column=0,row=0)

#Create Button
my_button=tk.Button(parent,text='Quit',height=1,width=35,command=parent.destroy)
my_button.pack()

#Add Canvas in Window
canvas_width=600
canvas_height=300
w=tk.Canvas(parent,width=canvas_width,height=canvas_height,bg="blue")
w.pack()

#Draw a line in Canvas
y=int(canvas_height/2)
w.create_line(15, 25, 200, 25) #Given X & Y Coodinates
w.create_line(55, 85, 155, 85, 105, 180, 55, 85) #Draw the triagle
w.create_line(300, 35, 300, 200, dash=(4, 2)) #Draw a dashed line

# Start GUI
parent.mainloop()
