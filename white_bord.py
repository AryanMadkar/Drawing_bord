from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk

win = Tk()
win.title("White Bord")
win.geometry("1050x570+150+50")
win.resizable(False,False)


current_x = 0
current_y = 0
color = "black"

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y
    canvas1.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas1.delete("all")
    display_pallet()

win.config(bg="black")
pig = Image.open("tkinter_projects\pig.png")
res_image = pig.resize((100,500),resample=3)

img = ImageTk.PhotoImage(res_image)
lb = Label(win,image=img,bg="black")
lb.place(x=20,y=20)


# erasser = PhotoImage(file="tkinter_projects\rubber.png")
erraser = Image.open("tkinter_projects/rubber.png")
res_errer = erraser.resize((40, 40),resample=3)
img1 = ImageTk.PhotoImage(res_errer)
gear = Button(win,bg="yellow",image=img1,command=new_canvas)
gear.place(x=50,y=400)


colors = Canvas(win,bg="white",width=40,height=300,bd=0)
colors.place(x=51,y=83)

def display_pallet():
    id = colors.create_rectangle((10,10,30,30),fill="red")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("Red"))
    
    id = colors.create_rectangle((10,40,30,60),fill="Blue")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("Blue"))
    
    id = colors.create_rectangle((10,70,30,90),fill="green")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("green"))
    
    id = colors.create_rectangle((10,100,30,120),fill="purple")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("Purple"))

    id = colors.create_rectangle((10,130,30,150),fill="black")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("black"))
    
    id = colors.create_rectangle((10,160,30,180),fill="pink")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("pink"))
    
    id = colors.create_rectangle((10,190,30,210),fill="white")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("white"))  
    
    id = colors.create_rectangle((10,220,30,240),fill="Brown")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("Brown"))
    
    id = colors.create_rectangle((10,250,30,270),fill="orange")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("orange"))
    
    id = colors.create_rectangle((10,280,30,300),fill="grey")
    colors.tag_bind(id,"<Button-1>",lambda x: show_color("grey"))
    
    
display_pallet()

canvas1 = Canvas(win,bg="white",width=870,height=500,cursor="hand2")
canvas1.place(x=140,y=30)
canvas1.bind("<Button-1>",locate_xy)
canvas1.bind("<B1-Motion>",addLine)



#####slider #################################

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_change(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()
slider = ttk.Scale(win,from_=0, to=20 ,orient = "horizontal",command =slider_change ,variable=current_value)
slider.place(x=20,y=530)


value_label = ttk.Label(win,text=get_current_value())
value_label.place(x=27,y=550)


win.mainloop()
