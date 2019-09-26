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
root.mainloop()
