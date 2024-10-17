from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter import ttk

window = Tk()
global selected
selected = False
def submit():
    input = text.get("1.0",END)
    print(input)
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\tungp\\Documents",
                                          title ="Select A File",
                                          filetype=[
                                            ("Text file",".txt"),
                                            ("HTML file",".html"),
                                            ("All file",".*")
                                          ])
    text_file = open(filepath, "r")
    stuff = text_file.read()
    text.insert(END, stuff)
    text_file.close()
def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\tungp\\Documents",
                                    defaultextension=".txt",
                                    filetype=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("All file",".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()
def cut_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    else:
        if text.selection_get():
            selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            window.clipboard_clear()
            window.clipboard_append(selected)
def copy_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    if text.selection_get():
        selected = text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)
def paste_text(e):
    global selected
    if e:
        selected = window.clipboard_get()
    else:
        if selected:
            position = text.index(INSERT)
            text.insert(position, selected)
def exitFile():
    ans = messagebox.askyesno("Save on close","Do you want to save file before closing?")
    if ans:
        window.destroy()
first_frame = Frame(window)
first_frame.pack(fill=BOTH, expand=1)
canvas = Canvas(first_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar = ttk.Scrollbar(first_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e:canvas.configure(scrollregion = canvas.bbox("all")))
second_frame = Frame(canvas)
canvas.create_window((0,0), window = second_frame, anchor = "nw")
scrollbar = ttk.Scrollbar(window, orient = 'horizontal')
scrollbar.config(command = canvas.xview)
scrollbar.pack(side = BOTTOM, fill = X)
canvas.config(xscrollcommand = scrollbar.set)
text = Text(second_frame,
            font=("Ink Free",25),
            bg="light yellow",
            fg="purple",
            undo=True,)
text.pack()
"""icon = PhotoImage(file="C:\\Users\\tungp\\OneDrive\\Máy tính\\.py file\\notepadicon.png")"""
"""window.iconphoto(True,icon)"""
menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,accelerator=("Ctrl+O"))
fileMenu.add_command(label="Save",command=saveFile,accelerator=("Ctrl+S"))
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exitFile,accelerator=("Alt+F4"))

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=lambda:cut_text(False),accelerator=("Ctrl+X"))
editMenu.add_command(label="Copy",command=lambda:copy_text(False),accelerator=("Ctrl+C"))
editMenu.add_command(label="Paste",command=lambda:paste_text(False),accelerator=("Ctrl+Y"))
editMenu.add_separator()
editMenu.add_command(label="Undo",command=text.edit_undo,accelerator=("Ctrl+Z"))
editMenu.add_command(label="Redo",command=text.edit_redo,accelerator=("Ctrl+Y"))
window.state("zoomed")
window.title("Notepad")
window.config(background="light yellow")
window.mainloop()
