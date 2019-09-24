from tkinter import Tk, Button, Menu, Label
from tkinter import ttk

def show():

    tempList = [
        ['Jim', '0.10'], 
        ['Dave', '0.20'], 
        ['James', '0.20'], 
        ['Eden', '0.5']]
        
    tempList.sort(key=lambda e: e[1], reverse=True)

    for i, (name, score) in enumerate(tempList, start=1):
        listBox.insert("", "end", values=(i, name, score))


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

# create Treeview with 3 columns
cols = ('Овог', 'Нэр','Нас', 'Утас')
listBox = ttk.Treeview(window, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

Button(window, text="Show scores", width=15, command=show).grid(row=4, column=0)
Button(window, text="Close", width=15, command=exit).grid(row=4, column=1)

window.mainloop()
