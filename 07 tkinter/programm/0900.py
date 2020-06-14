from tkinter import *

window = Tk()
window.title('Бүртгэлийн программ')
window.geometry('350x200')
window.resizable(0,0)

# reg_no, owog, ner, utas
reg_no = StringVar()
owog = StringVar()
ner = StringVar()
utas = StringVar()

Label(window,text='Регистр:').grid(row=0, column=0)
Entry(window, textvariable=reg_no).grid(row=0, column=1)

Label(window,text='Овог:').grid(row=1, column=0)
Entry(window, textvariable=owog).grid(row=1, column=1)

Label(window,text='Нэр:').grid(row=2, column=0)
Entry(window, textvariable=ner).grid(row=2, column=1)

Label(window,text='Утас:').grid(row=3, column=0)
Entry(window, textvariable=utas).grid(row=3, column=1)

def user_save():
    print(reg_no.get(), owog.get(), ner.get(), utas.get())


Button(window, text='Хадгалах', command=user_save).grid(row=4, column=0)


window.mainloop()
