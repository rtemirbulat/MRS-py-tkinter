import tkinter as tk
from tkinter import *
import os
from os import listdir
from os.path import isfile, join
from tkinter import filedialog

root = tk.Tk()
files = []
OPTIONS = [
"Attorney Letter",
"Funding",
"Data Sheet",
"Picture"
]
listbox = Listbox(root,width = 20, height=20, selectmode="SINGLE")
listbox.pack(side=LEFT,fill=BOTH)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

#canvas = tk.Canvas(root,height = 700, width = 700,bg = "#263D42")
#canvas.pack()

frame= tk.Frame(root,bg="gray")
frame.pack(side=LEFT,fill=BOTH)

#fills listbox with files in curr dir


def OpenDir():
    current_directory = filedialog.askdirectory()
    #filename = filedialog.askopenfilename(initialdir=current_directory,title="Select File",
    #                                      filetypes=(("PDFs","*.pdf"),("all files","*.*")))
    for widget in listbox.winfo_children():
        widget.destroy()

    #files.append(filename)
    #print(filename)
    for file in os.listdir(current_directory):
        listbox.insert(END, file)
    #listbox = Listbox(frame)
    #for name in files(current_directory):
     #   listbox.insert('end', name)
    #label = tk.Label(frame, text=files, bg ="gray")
    #label.pack()
    #listbox.pack()

appendix = StringVar(root)
#appendix.set(OPTIONS[0]) # default value
dropdown = OptionMenu(root,appendix, *OPTIONS)
dropdown.pack()
label = tk.Label(frame, bg ="gray")
label.pack()
#is_selected=False

def selected_item(event):
    #curr = listbox.curselection()
    #ass = (listbox.get(curr))
    #label = tk.Label(frame, text=ass, bg ="gray")
    #label.pack()

    #global is_selected
    #if is_selected:
     #   return
    #else:
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    label.config(text=picked)
        #is_selected = True
        #RenameFile(picked)
        #return is_selected


def RenameFile():
    temp = appendix.get()
    file_to_rename = listbox.get( listbox.curselection() )
    new_name = "GGG" + " " + temp
    try:
        os.rename(file_to_rename, new_name + ".pdf")
    except FileExistsError:
        n = 2
        ending = file_to_rename.split('/')[-1]
        if(ending=="2"):
            n = n + 1
        os.rename(file_to_rename, new_name + str(n) + ".pdf")



def Save():
    listbox.delete(0, END)
    label.config(text="")
    Label(root, text="success",
          font=('TkheadingFont, 20')).pack()



listbox.bind('<<ListboxSelect>>',selected_item)


listbox.pack()
rename = tk.Button(root, text='Rename',padx=10,pady=20, command=RenameFile, width=10,bg='brown',fg='white')

rename.pack()

save = tk.Button(root, text='Save',padx=10,pady=20, command=Save, width=10,bg='brown',fg='white')
save.pack()

openFile = tk.Button(root,text="Open Dir",padx=10,pady=20,fg="white",bg="#263D42", command=OpenDir)
openFile.pack()

root.mainloop()