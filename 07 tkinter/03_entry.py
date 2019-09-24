# Entry - бичвэр оруулах хэсэг
from tkinter import *

window = Tk()
window.title("Гарчиг")
window.geometry("290x392")
window.resizable(0, 0)

result_string = StringVar()


def hello():
    print(result_string.get())
    result_string.set('')


L1 = Label(window, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(window, bd=5, textvariable=result_string)
E1.pack(side=RIGHT)

B = Button(window, text="Hello", command=hello)
B.pack()

window.mainloop()
