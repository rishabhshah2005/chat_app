from tkinter import *
from funcs import *

root = Tk()
root.geometry('500x500')

FONT = ('helvetica', 15)



blnk_lab = Label(root, text='').grid(row=0, columnspan=3, pady=25)

# SERVER ADDRESS
server_lab = Label(root, text="Server: ", font=('helvetica', 15), padx=15, pady=20).grid(column=0, row=1)
s = StringVar()
server_add = Entry(root, width=20, font=('helvetica', 15), textvariable=s).grid(column=1, row=1)

# ENTER PORT
p = IntVar()
p.set('')
port_lab = Label(root, text="Port: ", font=('helvetica', 15), padx=15, pady=20).grid(column=0, row=2)
port_ent = Entry(root, width=20, font=('helvetica', 15), textvariable=p).grid(column=1, row=2)

# ENTER NAME
nm = StringVar()
name_lab = Label(root, text="Your Name: ", font=('helvetica', 15), padx=15, pady=20).grid(column=0, row=3)
name_ent = Entry(root, width=20, font=FONT, textvariable=nm).grid(column=1, row=3)

# BUTTON
btn = Button(root, text='Connect', font=FONT, padx=30, pady=20, command=lambda: connect(root, ip=s.get(), port=p.get(), nickname=nm.get())).grid(column=0, row=4, columnspan=4, padx=25, pady=30)

root.mainloop()
