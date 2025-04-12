from tkinter import *
expression =""
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=""

    except:
        equation.set(" error ")
        expression=""


def clear():
    global expression
    expression =""
    equation.set("")



if __name__=="__main__":
    gui=Tk()
    gui.configure(bg="light green")
    gui.title("simple calculator")
    gui.geometry("300x300")
    equation = StringVar()

    expression_field =Entry(gui,textvariable=equation)
    expression_field.grid(columnspan=5,ipady=10,ipadx=30)
    b1=Button(gui,text='1',fg='black',bg='white',command=lambda: press(1),height=1,width=7)
    b1.grid(row=2,column=0)
    b2=Button(gui,text='2',fg='black',bg='white',command=lambda: press(2),height=1,width=7)
    b2.grid(row=2,column=1)
    b3=Button(gui,text='3',fg='black',bg='white',command=lambda: press(3),height=1,width=7)
    b3.grid(row=2,column=2)
    b4=Button(gui,text='4',fg='black',bg='white',command=lambda: press(4),height=1,width=7)
    b4.grid(row=3,column=0)
    b5=Button(gui,text='5',fg='black',bg='white',command=lambda: press(5),height=1,width=7)
    b5.grid(row=3,column=1)
    b6=Button(gui,text='6',fg='black',bg='white',command=lambda: press(6),height=1,width=7)
    b6.grid(row=3,column=2)
    b7=Button(gui,text='7',fg='black',bg='white',command=lambda: press(7),height=1,width=7)
    b7.grid(row=4,column=0)
    b8=Button(gui,text='8',fg='black',bg='white',command=lambda: press(8),height=1,width=7)
    b8.grid(row=4,column=1)
    b9=Button(gui,text='9',fg='black',bg='white',command=lambda: press(9),height=1,width=7)
    b9.grid(row=4,column=2)
    b11=Button(gui,text='0',fg='black',bg='white',command=lambda: press(0),height=1,width=7)
    b11.grid(row=5,column=0)
    b12=Button(gui,text='+',fg='black',bg='white',command=lambda: press('+'),height=1,width=7)
    b12.grid(row=5,column=1)
    b13=Button(gui,text='-',fg='black',bg='white',command=lambda: press('-'),height=1,width=7)
    b13.grid(row=5,column=2)
    b14=Button(gui,text='*',fg='black',bg='white',command=lambda: press('*'),height=1,width=7)
    b14.grid(row=6,column=0)
    b15=Button(gui,text='/',fg='black',bg='white',command=lambda: press('/'),height=1,width=7)
    b15.grid(row=6,column=1)
    b16=Button(gui,text='%',fg='black',bg='white',command=lambda: press('%'),height=1,width=7)
    b16.grid(row=6,column=2)
    b17=Button(gui,text='=',fg='black',bg='white',height=1,width=7,command=equalpress)
    b17.grid(row=7,column=0)
    b18=Button(gui,text="clear",fg='black',bg='white',height=1,width=7,command=clear)
    b18.grid(row=7,column=1)
    gui.mainloop()


