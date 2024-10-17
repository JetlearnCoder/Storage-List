from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

window = Tk()
window.geometry("750x300")
window.config(bg = "white")

openbutton = Button(window,text = "Open")
addbutton = Button(window,text = "Add")
savebutton = Button(window,text = "Save")
deletebutton = Button(window,text = "Delete")

frame = Frame(window)
frame.pack(side = BOTTOM)
listed = ["a","b","cde"]
scrlbar = Scrollbar(frame,orient = "vertical")

listbox = Listbox(frame,width = 45,yscrollcommand = scrlbar.set, bg = "grey")
for i in range(500):
    listbox.insert(END,"LIST "+str(i))

openbutton.place(x = 20, y = 110)
addbutton.place(x = 300, y = 70)
savebutton.place(x = 300, y = 20)
deletebutton.place(x = 600, y = 110 )
listbox.pack(side = LEFT, padx = 5)
scrlbar.pack(side = RIGHT, pady = 5)
scrlbar.config(command = listbox.yview)


window.mainloop()