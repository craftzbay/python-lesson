from tkinter import Tk, Button, Menu, Label
from tkinter import ttk

def showData():

    data = [
        ['Bat', 'Bold','26','99455623'], 
        ['Bat', 'Bold','26','99455623'], 
        ['Bat', 'Bold','26','99455623'],  
        ['Bat', 'Bold','26','99455623']
    ]

    # data.sort(key=lambda e: e[0], reverse=True)

    for i in data:
        listBox.insert("", "end", values=i)


def menuClicked():
    print('menu daragdsan')

window = Tk()
window.title('Бүртгэлийн программ')
window.geometry('805x500')
window.resizable(0,0)


menubar = Menu(window)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Бүртгэх", command=menuClicked)
menu.add_command(label="Засварлах", command=menuClicked)
menu.add_command(label="Устгах", command=menuClicked)
menu.add_separator()
menu.add_command(label="Гарах", command=window.quit)
menubar.add_cascade(label="Цэс", menu=menu)

Label(window, text="Мэдээллийн жагсаалт", font=("Arial",14)).grid(row=0, columnspan=3)
window.config(menu=menubar)


cols = ('Овог', 'Нэр','Нас', 'Утас')
listBox = ttk.Treeview(window, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=2, column=0, columnspan=2)

showData()
window.mainloop()
