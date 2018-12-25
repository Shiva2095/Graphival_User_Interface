import tkinter as tk
def write_slogan():
    print("Tkinter Is easy to Learn .")
    
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,
                 text="Quit",
                 fg="red",
                 command=quit)
button.pack(side=tk.LEFT)

slogan=tk.Button(frame,
                 text="Hello",
                 fg="green",
                 command=write_slogan)
slogan.pack(side=tk.LEFT)
root.mainloop()

