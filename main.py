import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from ttkwidgets.autocomplete import AutocompleteCombobox

root = tk.Tk()
root.geometry("1350x540")
files = []
OPTIONS = [
    "Attorney Letter",
    "Funding",
    "Data Sheet",
    "Picture",
    "Certification of Driver License",
    "Affidavit of No Insurance",
    "EUO",
    "Bill Summary",
    "Police Report",
    "Patient Information",
    "Insurance card",
    "Insurance Information",
    "Cover Letter",
    "POM",
    "Consent to Change Attorney",
    "Law Agreement",
    "Medical records",
    "Law Verification",
    "Funding Agreement",
    "Intake Form",
    "NF-2",
    "Insurance Letter",
    "Email receipt",
    "Email from Attorney",
    "Email Confirmation",
    "Retainer Statement",
    "Liens",
    "Attorney Evaluation letter",
    "Attorney Agreement",
    "Notice of Denial",
    "NF-10","Peer Review","EOR", "Plaintiff's Response to Demands", "Plaintiff's Verified Answer", "Medical Reports and Doctor's lien",
    "Notice of designation and appearance","Notice of appearance, Verified Answer","Notice of entry","Amended Verified Answer","Notice of motion","Verified Answer","MRI Examination","Summary of Service Charges","Invoice ","Hospital Notice","Compliance Conference order","Acknowledgment of Representation","Affidavit of Service ","Entity Information","Driver Record ","NYSCEF Payment Receipt","Appearance report","Notice of Approval","Notice of Case Assembly","Irrevocable Letter of Direction","HIPAA authorization","IME Notice","Notice of Electronic Filing","Preliminary Conference Order and Case Scheduling","Request for Judicial intervention","Third-party Summons","Contract for advance payment","NF-6","Summons","Notice of motion for default judgement","Verified Bill of Particulars","Purchase Agreement","Notice of Petition","EBT (Examination before trial)","Request for Judicial Intervention",
    
    
    
    
    
]

data = [
   
]

#fax variable
fax= IntVar()
# fills listbox with files in curr dir
def OpenDir():
    listbox.delete(0, END)
    current_directory = filedialog.askdirectory()
    for file in os.listdir(current_directory):
        listbox.insert(END, file)
    folder_lb.config(text=os.path.abspath(current_directory))

#function to display current file
def selected_item(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    label.config(text=picked)
#opens popup when file already moved
def open_popup():
    top = Toplevel(root)
    top.geometry("120x70")
    top.title("FileNotFoundError")
    Label(top, text="File already removed & moved or does not exist!").place(x=0, y=0)
#main renaming function
def RenameFile():
    file_to_rename = label['text']
    working_dir = folder_lb['text']
    custom = inputtxt.get("1.0", "end")
    type = entry4.get()
    if fax.get():
        new_name = entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + custom.strip() + " " + type +" FAX "
    else:
        new_name = entry1.get() + " " + entry2.get() + " " + entry3.get() + " " + custom.strip() + " " + type
    try:
        os.rename(working_dir + "/" + file_to_rename, working_dir + "/" + new_name + ".pdf")
    except FileExistsError:
        index = ''
        while True:
            try:
                os.rename(working_dir + "/" + file_to_rename,working_dir+"/"+ new_name+index+".pdf")
                break
            except WindowsError:
                if index:
                    index = '(' + str(int(index[1:-1]) + 1) + ')'  # Append 1 to number in brackets
                else:
                    index = '(1)'
                pass

    except FileNotFoundError:
        open_popup()
#clear selections
def Clear():
    inputtxt.delete('1.0', END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)#choose option reset
    label.config(text="")

# frame for selection and selection label with scrollbar
listbox = Listbox(root, width=40, height=300, selectmode="SINGLE")
listbox.pack(side=LEFT, padx=30, pady=30, fill=NONE)
scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
frame = tk.Frame(root, padx=10, pady=20, bg="white")
frame.pack(anchor="n", after=listbox, side=TOP)
# Label of listbox
files_label = tk.Label(root, text="Files: ", bg="white").pack(anchor=NW, padx=30, ipadx=20, ipady=2, before=listbox)

# label of selection
fr = tk.Frame(root, borderwidth=1, bg="white")
fr.pack(anchor="nw")
selected = tk.Label(fr, bg="white", text="Выбранный файл:")
selected.pack(anchor="nw", side=LEFT)
label = tk.Label(fr, bg="#dbdbdb", width=40)  # displays selected file
label.pack(anchor="nw", padx=10, pady=10, side=LEFT)

# label of folder
folder = tk.Label(fr, bg="white", text="Папка:")
folder.pack(anchor="nw", side=LEFT)
folder_lb = tk.Label(fr, bg="#dbdbdb", width=50)
folder_lb.pack(anchor="nw", padx=10, pady=10, side=LEFT)

# renameto
rename = tk.Label(root, text="Переименовать на:")
rename.pack(anchor="nw", side=TOP, padx=5, pady=5)

# frame with selection
fr2 = tk.Frame(root, borderwidth=2, bg="white")
fr2.pack(anchor="nw", after=rename)
patients = tk.Label(fr2, bg="white", text="Клиенты :")
patients.pack(anchor="nw", side=LEFT)
entry1 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry1.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry2 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry2.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry3 = AutocompleteCombobox(fr2, width=30, completevalues=data)
entry3.pack(side=LEFT, padx=10, pady=10, anchor="nw")
fax_c = Checkbutton(fr2,text="FAX?",variable=fax,onvalue=1,offvalue=0)
fax_c.pack(side=LEFT, padx=10, pady=10, anchor="nw")


# frame of custom input
fr3 = tk.Frame(root, borderwidth=2, bg="white")
fr3.pack(anchor="nw", after=fr2, pady=10)
# custom_input
custom_input = tk.Label(fr3, bg="white", text="Свободный ввод :")
custom_input.pack(anchor="nw", side=LEFT)
inputtxt = tk.Text(fr3, height=1, width=40)
inputtxt.pack(side=LEFT, padx=10, pady=10, anchor="nw")

# frame type of file
fr4 = tk.Frame(root, borderwidth=2, bg="white")
fr4.pack(pady=10, padx=5, side=RIGHT, after=fr2, anchor="n")
type_input = tk.Label(fr4, bg="white", text="Тип документа :")
type_input.pack(anchor="nw", side=LEFT)
#dropdown = OptionMenu(fr4, appendix, *OPTIONS)
#dropdown.config(width=10)
#dropdown.pack(side=LEFT, padx=10, pady=10, anchor="nw")
entry4 = AutocompleteCombobox(fr4, width=50, completevalues=OPTIONS)
entry4.pack(side=LEFT, padx=10, pady=10, anchor="nw")


# buttons

rename = tk.Button(root, text='Переименовать', padx=10, pady=20, command=RenameFile, width=10, bg='brown', fg='white')
rename.pack(side=RIGHT, padx=10, pady=10, after=fr, anchor="n")

clear = tk.Button(root, text='Очистить', padx=10, pady=20, command=Clear, width=10, bg='brown', fg='white')
clear.pack(side=LEFT, padx=5, pady=10, anchor="nw")

openFile = tk.Button(root, text="Open Folder", padx=10, pady=20, fg="white", bg="#263D42", command=OpenDir)
openFile.pack(side=RIGHT, padx=5, pady=10, anchor="nw")

listbox.bind('<<ListboxSelect>>', selected_item)
listbox.pack()

root.mainloop()
