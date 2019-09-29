from tkinter import Tk,Frame,StringVar,Label,Entry,Button
from tkinter import LEFT,RIGHT,BOTTOM,TOP

window = Tk() # window нэтрэй object үүсгэсэн
window.title('Бүртгэлийн программ') # гарчиг
window.geometry('{}x{}'.format(800,500)) # цонхны хэмжээ
window.resizable(0,0) # цонхны хэмжээг өөрчлөх боломжгүй болгох

# Цонх grid болгож хуваах тохиргоо
# window.grid_rowconfigure(100, weight=1)
# window.grid_columnconfigure(14, weight=1)

owog = StringVar()
ner = StringVar()

# Үндсэн цонхоо баруун болон зүүн хэсгүүдэд хуваах
zuun_tal = Frame(window,width=300,height=500)
barun_tal = Frame(window,width=600, height=500,bg='yellow')
zuun_tal.pack(side=LEFT)
barun_tal.pack(side=RIGHT)


Label(zuun_tal, text="Овог:").grid(row=0, column=0)
Entry(zuun_tal, textvariable=owog).grid(row=0, column=1)
Label(zuun_tal, text="Нэр:").grid(row=1, column=0)
Entry(zuun_tal, textvariable=owog).grid(row=1, column=1)
Label(zuun_tal, text="Нас:").grid(row=2, column=0)
Entry(zuun_tal, textvariable=owog).grid(row=2, column=1)
Label(zuun_tal, text="Утас:").grid(row=3, column=0)
Entry(zuun_tal, textvariable=owog).grid(row=3, column=1)

def save():
    print('save')
def cancel():
    print('cancel')

Button(zuun_tal,text="Хадгалах",command=save).grid(row=5,column=0)
Button(zuun_tal,text="Цуцлах",command=cancel).grid(row=5,column=1)

window.mainloop()
