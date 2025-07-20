import tkinter as tk 
from time import strftime 

root = tk.Tk() 
root.title("DIGITAL CLOCK")

title_label = tk.Label(root, text="DIGITAL CLOCK", font=('Space Mono', 60, 'bold'), bg='#22272d', fg='white')
title_label.pack(anchor='center', fill='both')

def time():
    str_time = strftime('%r\n%b %d,%Y')
    label.config(text=str_time)
    label.after(1000, time)

label = tk.Label(root, font=('Space Mono', 70, 'bold'), bg='#22272d' , fg='white') 
label.pack(anchor='center' , fill='both' , expand=True) 

time()
root.mainloop() 
