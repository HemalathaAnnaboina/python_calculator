from tkinter import *

def fun():
    nu1=3
    nu2=4
    result=nu1+nu2
    la.config(text=f"result: {result}")
    b.config(bg="pink",font=("hasattr",12),fg="yellow",text="data was stored")
root=Tk()


l1=Label(root,text="enter a 1st number:  ")
l1.grid(row=1,column=0)
n1=Entry()
n1.grid(row=1,column=1)
l2=Label(root,text="enter a 2nd number:  ")
l2.grid(row=2,column=0)
n2=Entry()
n2.grid(row=2,column=1)

b=Button(root,text="click me",command=fun)
b.grid(row=3)
la=Label(root,text="")
la.grid(row=4)
root.mainloop()