from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

data = [
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    },
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    },
    {
        "owog":"Bat",
        "ner":"Bold",
        "nas": 26,
        "huis": "er",
        "utas": "99562312"
    }
]


root = Tk()
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 565
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


# Frames
top_frame = Frame(root, bg='white', width=450, height=30, pady=3).grid(row=0, sticky="ew")
center = Frame(root, bg='gray', width=50, height=40, padx=3, pady=3).grid(row=1, sticky="nsew")



def menuClicked():
    print('menu daragdsan')

menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Бүртгэх", command=menuClicked)
menu.add_command(label="Засварлах", command=menuClicked)
menu.add_command(label="Устгах", command=menuClicked)
menu.add_separator()
menu.add_command(label="Гарах", command=root.quit)
menubar.add_cascade(label="Цэс", menu=menu)
# display the menu
root.config(menu=menubar)


model_label = Label(top_frame, text='Жагсаалт', font=(
    "Arial", 14))
model_label.grid(row=0, columnspan=3)


table = ttk.Treeview(
    center, columns=("Овог", "Нэр", "Нас", "Хүйс", "Утас"),
                    selectmode="extended", height=500)

table.heading('Овог', text="Овог", anchor=W)
table.heading('Нэр', text="Нэр", anchor=W)
table.heading('Нас', text="Нас", anchor=W)
table.heading('Хүйс', text="Хүйс", anchor=W)
table.heading('Утас', text="Утас", anchor=W)
table.column('#0', stretch=NO, minwidth=0, width=0)
table.column('#1', stretch=NO, minwidth=0, width=80)
table.column('#2', stretch=NO, minwidth=0, width=120)
table.column('#3', stretch=NO, minwidth=0, width=80)
table.column('#4', stretch=NO, minwidth=0, width=150)
table.column('#5', stretch=NO, minwidth=0, width=120)
table.grid(row=1,column=0)

def Read():
    table.delete(*table.get_children())

    for d in data:
        table.insert('', 'end', values=(d["owog"], d["ner"], d["nas"], d["huis"], d["utas"]))


Read()
root.mainloop()
