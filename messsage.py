import tkinter as tk

master=tk.Tk()
master.title("Message Box")
whatever_u_do="What Ever You Do Will be insignificat ,butit is very important u do it \n (Mahatma Gandhi)"
msg=tk.Message(master,text=whatever_u_do)
msg.config(bg='light green',font=('times',24,'italic'))
msg.pack()
tk.mainloop()
