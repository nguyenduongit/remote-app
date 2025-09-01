#!/usr/bin/env python3
import tkinter as tk

root = tk.Tk()
root.title("Hello World")
label = tk.Label(root, text="Hello World!", font=("Arial", 20))
label.pack(padx=50, pady=50)
root.mainloop()
