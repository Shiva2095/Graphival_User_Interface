from tkinter import *
master =Tk()
def show_states():
    print("First Name : %s \n last Name : %s" %(e1.get(),e2.get()))
    e1.delete(0,END)
    e2.delete(0,END)
    
Label(master,text="First Name :").grid(row=0)
Label(master,text="Last Name  :").grid(row=1)

e1=Entry(master)
e2=Entry(master)
e1.insert(10,"Varsha")
e2.insert(10,"Agrawal")

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

Button(master,text="Quit" ,command=master.quit).grid(row=2,column=0,sticky=W,pady=5,padx=5)
Button(master,text="Show",command=show_states).grid(row=2,column=1,stick=W,pady=5,padx=5)
mainloop()
