from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

window = Tk() # window нэтрэй object үүсгэсэн
window.title('Бүртгэлийн программ') # гарчиг
window.geometry('{}x{}'.format(800,500)) # цонхны хэмжээ
window.resizable(0,0) # цонхны хэмжээг өөрчлөх боломжгүй болгох

# Цонх grid болгож хуваах тохиргоо
# window.grid_rowconfigure(100, weight=1)
# window.grid_columnconfigure(14, weight=1)

owog = StringVar()
ner = StringVar()
nas = StringVar()
utas = StringVar()

# Үндсэн цонхоо баруун болон зүүн хэсгүүдэд хуваах
zuun_tal = Frame(window,width=300,height=500)
barun_tal = Frame(window,width=600, height=500,bg='yellow')
zuun_tal.pack(side=LEFT)
barun_tal.pack(side=RIGHT)


Label(zuun_tal, text="Овог:").grid(row=0, column=0)
Entry(zuun_tal, textvariable=owog).grid(row=0, column=1)

Label(zuun_tal, text="Нэр:").grid(row=1, column=0)
Entry(zuun_tal, textvariable=ner).grid(row=1, column=1)

Label(zuun_tal, text="Нас:").grid(row=2, column=0)
Entry(zuun_tal, textvariable=nas).grid(row=2, column=1)

Label(zuun_tal, text="Утас:").grid(row=3, column=0)
Entry(zuun_tal, textvariable=utas).grid(row=3, column=1)

def save():
    table.insert('', 'end', 
    values=(owog.get(),ner.get(),nas.get(),utas.get()))
    owog.set('')
    ner.set('')
    nas.set('')
    utas.set('')
def cancel():
    owog.set('')
    ner.set('')
    nas.set('')
    utas.set('')

Button(zuun_tal,text="Хадгалах",command=save).grid(row=6,column=0)
Button(zuun_tal,text="Цуцлах",command=cancel).grid(row=6,column=1)


table = ttk.Treeview(barun_tal, 
columns=("Овог", "Нэр", "Нас", "Утас"),
selectmode="extended", height=500)
table.heading('Овог', text="Овог", anchor=W)
table.heading('Нэр', text="Нэр", anchor=W)
table.heading('Нас', text="Нас", anchor=W)
table.heading('Утас', text="Утас", anchor=W)
table.column('#0', stretch=NO, minwidth=0, width=0)
table.column('#1', stretch=NO, minwidth=0, width=150)
table.column('#2', stretch=NO, minwidth=0, width=150)
table.column('#3', stretch=NO, minwidth=0, width=100)
table.column('#4', stretch=NO, minwidth=0, width=300)
table.pack()

table.insert('', 'end', values=("Bat","Dorj","26","89895623"))

window.mainloop()
