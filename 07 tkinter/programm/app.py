from tkinter import Tk, Button, Menu, Label


def menuClicked():
    print('menu daragdsan')

window = Tk()
window.title('Бүртгэлийн программ')
window.geometry('400x500')


menubar = Menu(window)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Бүртгэх", command=menuClicked)
menu.add_command(label="Засварлах", command=menuClicked)
menu.add_command(label="Устгах", command=menuClicked)
menu.add_separator()
menu.add_command(label="Гарах", command=window.quit)
menubar.add_cascade(label="Цэс", menu=menu)

Label(window, text="Мэдээллийн жагсаалт", 
    font=("Arial",14)).grid(row=0, columnspan=3)
window.config(menu=menubar)
window.mainloop()
