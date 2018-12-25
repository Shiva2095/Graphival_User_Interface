import tkinter as tk
root=tk.Tk()
v=tk.IntVar()
v.set(1)
languages=[("Python",1),("Java",2),("c",3),("CPP",4)]
def showchoice():
    print(v.get())
    
tk.Label(root,
         text=""" Choose Your languages
to work On """,
         justify=tk.LEFT,
         padx=20,
         ).pack()
for val,language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   indicatoron=0,
                   width=20,
                   variable=v,
                   command=showchoice,
                   value=val).pack(anchor=tk.W)
root.mainloop()
