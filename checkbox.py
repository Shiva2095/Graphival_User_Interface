from tkinter import*

master=Tk()
def var_show():
    print("Variable1 : %d \n Variable2 : %d "%(var1.get(),var2.get()))
Label(master,text="This Is For CheckBox : ").grid(row=0,sticky=W)
var1=IntVar()
Checkbutton(master,text="Python",variable=var1).grid(row=1,sticky=W)
var2=IntVar()
Checkbutton(master,text="java",variable=var2).grid(row=3,sticky=W)
Button(master,text="Quit",command=master.quit).grid(row=4,sticky=W)
Button(master,text="Show",command=var_show).grid(row=5,sticky=W)

mainloop()
