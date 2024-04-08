import tkinter as tk
from tkinter import*

root=tk.Tk()
root.title("Calculator")
root.geometry("410x440+200+100")
root.resizable(False,False)
root.configure(bg="#29AB87")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
def det():
    global equation
    equation=equation[:-1]
    label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result=eval(equation)
        except:
          result="error"
          equation=""
        label_result.config(text=result)
    

Image_icon=PhotoImage(file="calculator.png")
root.iconphoto(False,Image_icon)

label_result=Label(root,width=20,height=2,text="",font=("arial",20),bg="white", fg="black", bd=5, relief="groove")
label_result.pack(pady=20)

Button(root,text="C", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="red",command=lambda: clear()).place(x=10,y=110)
Button(root,text="DEL", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="gray",command=lambda:det()).place(x=110,y=110)
Button(root,text="/", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="gray",command=lambda:show("/")).place(x=210,y=110)
Button(root,text="%", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="gray",command=lambda:show("%")).place(x=310,y=110)

Button(root,text="7", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("7")).place(x=10,y=170)
Button(root,text="8",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("8")).place(x=110,y=170)
Button(root,text="9", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("9")).place(x=210,y=170)
Button(root,text="*", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("*")).place(x=310,y=170)

Button(root,text="4", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("4")).place(x=10,y=230)
Button(root,text="5", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("5")).place(x=110,y=230)
Button(root,text="6", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("6")).place(x=210,y=230)
Button(root,text="-", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("-")).place(x=310,y=230)

Button(root,text="1", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("1")).place(x=10,y=290)
Button(root,text="2", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("2")).place(x=110,y=290)
Button(root,text="3", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("3")).place(x=210,y=290)
Button(root,text="+", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("+")).place(x=310,y=290)

Button(root,text="0", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show("0")).place(x=10,y=350)
Button(root,text=".", width=5,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:show(".")).place(x=110,y=350)
Button(root,text="=", width=11,height=1,font=("arial",20,"bold"),bd=1,fg="white",bg="grey",command=lambda:calculate()).place(x=210,y=350)

root.mainloop()