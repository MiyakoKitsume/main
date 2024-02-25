#Import library
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
#Creating windows
main = Tk()
global Selected
Selected = False
#Making tools
def submit():
    #Input from the keyboard
    input = text.get("1.0", END)
    print(input)
def openFile():
    filepath = filedialog.askopenfilename(initialdir = "C:\\Users\\ASUS\\PycharmProjects\\pythonProject1",
                                          title = "Select a file",
                                          filetypes = [
                                              ("Text file",".txt"),
                                              ("HTML file",".HTML"),
                                              ("All file","*")
                                          ])
    text_file = open(filepath, "w")
    items = text_file.read()
    text.insert(END, items)
    text_file.close()
def saveFile():
    file = filedialog.asksaveasfilename(initialdir = "C:\\Users\\ASUS\\PycharmProjects\\pythonProject1",
                                        defaultextension = ".txt",
                                        filetypes = [
                                            ("Text file", ".txt"),
                                            ("HTML file", ".HTML"),
                                            ("All file", "*")
                                        ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()
def exitFile():
    ans = messagebox.askyesno("Save on close","Do you want to save file before closing?")
    if ans:
        main.destroy()
def cut(e):
    global Selected
    if e:
        Selected = main.clipboard_get()
    else:
        if text.selection_get():
            Selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            main.clipboard_clear()
            main.clipboard_append(Selected)
def copy(e):
    global Selected
    if e:
        Selected = main.clipboard_get()
    if text.selection_get():
        Selected = text.selection_get()
        main.clipboard_clear()
        main.clipboard_append(Selected)
def paste(e):
    global Selected
    if e:
        Selected = main.clipboard_get()
    else:
        if Selected:
            position = text.index(INSERT)
            text.insert(position, Selected)
def delete():
    text.delete("1.0", END)
def find_and_replace():

    find_text)

def find_text(*args):
    ind_label = Label(main, text = "Find")
    find_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    find_entry = Entry(main,width = 30)
    find_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    replace_label = Label(main, text = "Replace")
    replace_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    replace_entry = Entry(main,width = 30)
    replace_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    find_button = Button(main, text = "Find", command = f
    text_to_find = find_entry.get()
    if text_to_find:
        start_index = "1.0"
        while True:
            start_index = text.search(text_to_find, start_index, stopindex =END)
            if not start_index:
                break
            end_index = f"{start_index}+{len(text_to_find)}c"
            text.tag_add(SEL, start_index, end_index)
            start_index = end_index
#Making ajustments
newWin = Toplevel(main)
newWin.title("Find and replace")
newWin.geometry("300x200")
newWin.resizable(height = False, width = False)
first_frame = Frame(main)
first_frame.pack(fill = BOTH, expand = 1)
canvas = Canvas(first_frame)
canvas.pack(side = LEFT, fill = BOTH, expand = 1)
scollbar = ttk.Scrollbar(first_frame, orient = VERTICAL, command = canvas.yview())
scollbar.pack(side = RIGHT, fill = Y)
canvas.configure(yscrollcommand = scollbar.set)
canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion = canvas.bbox("all")))
second_frame = Frame(canvas)
canvas.create_window((0,0), window = second_frame, anchor = "nw")
scollbar = Scrollbar(main, orient = "horizontal")
scollbar.config(command = canvas.xview)
scollbar.pack(side = BOTTOM, fill = X)
canvas.config(xscrollcommand = scollbar.set)
text = Text(second_frame,
            font = ("Ink free", 25),
            bg = "black",
            fg = "pink",
            undo = True,)
text.pack()
#Creating menubar
menubar = Menu(main)
main.config(menu = menubar)
fileMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label = "Open", command = openFile, accelerator = ("Ctrl + O"))
fileMenu.add_command(label = "Save", command = saveFile, accelerator = ("Ctrl + S"))
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exitFile, accelerator = ("Alt + F4"))

fileMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = fileMenu)
fileMenu.add_command(label = "Cut", command = lambda :cut(False), accelerator = "Ctrl + X")
fileMenu.add_command(label = "Copy", command = lambda :copy(False), accelerator = "Ctrl + C")
fileMenu.add_command(label = "Paste", command = lambda :paste(False), accelerator = "Ctrl + V")
fileMenu.add_command(label = "Delete", command = delete, accelerator = "Delete")
fileMenu.add_separator()
fileMenu.add_command(label="Find and replace", command = find_and_replace , accelerator = "Ctrl + F")
fileMenu.add_separator()
fileMenu.add_command(label = "Undo", command = text.edit_undo, accelerator = ("Ctrl + Z"))
fileMenu.add_command(label = "Redo", command = text.edit_redo, accelerator = ("Ctrl + Y"))

#Configure windows
main.state("zoomed")
main.title("Notepad (Beta)")
main.config(background = "black")
main.mainloop()
