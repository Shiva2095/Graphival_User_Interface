import tkinter as tk
root=tk.Tk()
logo=tk.PhotoImage(file="python-logo.png")
explaination="""At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2=tk.Label(root,
            compound=tk.LEFT,
            image=logo,
            text=explaination).pack(side="right")

root.mainloop()
