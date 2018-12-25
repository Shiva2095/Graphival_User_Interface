import tkinter as tk

root=tk.Tk()
tk.Label(root,text="Hello head",
         fg="red",
         bg="green",
         font="Times").pack()
tk.Label(root,text="green text",
         fg="green",
         bg="red",
         font="Helvitica 16 bold italic").pack()
tk.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()
root.mainloop()

