from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Python: Simple CRUD Applition")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 700
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

top_frame = Frame(root, bg='white', width=450, height=50, pady=3).grid(row=0, sticky="ew")
center = Frame(root, bg='green', width=50, height=40, padx=3, pady=3).grid(row=1, sticky="nsew")
# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

def menuClicked():
    print('menu daragdsan')

menubar = Menu(top_frame)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Бүртгэх", command=menuClicked)
menu.add_command(label="Засварлах", command=menuClicked)
menu.add_command(label="Устгах", command=menuClicked)
menu.add_separator()
menu.add_command(label="Гарах", command=root.quit)
menubar.add_cascade(label="Цэс", menu=menu)
model_label = Label(top_frame, text='Model Dimensions')
model_label.grid(row=0, columnspan=3)


table = ttk.Treeview(
    center, columns=("Firstname", "Lastname", "Gender", "Address", "Username", "Password"),
                    selectmode="extended", height=500)

table.heading('Firstname', text="Firstname", anchor=W)
table.heading('Lastname', text="Lastname", anchor=W)
table.heading('Gender', text="Gender", anchor=W)
table.heading('Address', text="Address", anchor=W)
table.heading('Username', text="Username", anchor=W)
table.heading('Password', text="Password", anchor=W)
table.column('#0', stretch=NO, minwidth=0, width=0)
table.column('#1', stretch=NO, minwidth=0, width=80)
table.column('#2', stretch=NO, minwidth=0, width=120)
table.column('#3', stretch=NO, minwidth=0, width=80)
table.column('#4', stretch=NO, minwidth=0, width=150)
table.column('#5', stretch=NO, minwidth=0, width=120)
table.column('#6', stretch=NO, minwidth=0, width=120)
table.grid()

root.mainloop()
