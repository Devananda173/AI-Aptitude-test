from tkinter import*
mainwindow=Tk()
mainwindow.geometry('300x400')
Label(mainwindow,text='there are many flowers in my garden',fg='white',bg='green').pack(fill='x')
Label(mainwindow,text='Stay home,stay safe',fg='white',bg='blue',font=('Copperplate Gothic Bold',20)).pack(fill='x',pady=30,padx=40)
v=Entry(mainwindow,width=50,borderwidth=6)
v.pack()
print(v)
def on_click():
    try:
        x=v.get()
        print(x)
    except:
        pass
Button(mainwindow,text='click me',command=on_click).pack()
mainwindow.mainloop()
