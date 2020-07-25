from tkinter import *
import tkinter.messagebox as msgbox

window = Tk()
window.title("Гарчиг")
window.geometry("350x250")
window.resizable(0, 0)

selected_index = -1

register = StringVar()
lname = StringVar()
fname = StringVar()
phone = StringVar()

Label(window, text='Регистр').grid(row=0, column=0)
Entry(window, bd=1, textvariable=register).grid(row=1, column=0)

Label(window, text='Овог').grid(row=2, column=0)
Entry(window, bd=1, textvariable=lname).grid(row=3, column=0)

Label(window, text='Нэр').grid(row=4, column=0)
Entry(window, bd=1,textvariable=fname).grid(row=5, column=0)

Label(window, text='Утас').grid(row=6, column=0)
Entry(window, bd=1,textvariable=phone).grid(row=7, column=0)

def clear_entries():
    register.set('')
    lname.set('')
    fname.set('')
    phone.set('')

def save():
    if register.get()=='' or lname.get()=='' or fname.get()=='' or phone.get()=='':
        msgbox.showwarning('Анхаар', 'Мэдээлэл бүрэн оруулна уу')
    else:
        list_data.insert(END, register.get()+','+lname.get()+','+fname.get()+','+phone.get())
        clear_entries()

def delete():
    list_data.delete(list_data.curselection()[0])
    clear_entries()

def select(e):
    index = list_data.curselection()[0]
    selected = list_data.get(index)
    global selected_index
    selected_index = index
    
    data = selected.split(',')
    register.set(data[0])
    lname.set(data[1])
    fname.set(data[2])
    phone.set(data[3])

def update():
    if register.get()=='' or lname.get()=='' or fname.get()=='' or phone.get()=='':
        msgbox.showwarning('Анхаар', 'Мэдээлэл бүрэн оруулна уу')
    else:
        list_data.delete(selected_index)
        list_data.insert(selected_index, register.get()+','+lname.get()+','+fname.get()+','+phone.get())
        clear_entries()


Button(window, text='Бүртгэх', command=save).grid(row=8, column=0)
Button(window, text='Арилгах', command=clear_entries).grid(row=8, column=1)
Button(window, text='Устгах', command=delete).grid(row=8, column=2)
Button(window, text='Засах', command=update).grid(row=8, column=3)

list_data = Listbox(window, width=38, height=10)
list_data.grid(row=0, rowspan=8, column=1, columnspan=4)
list_data.bind('<<ListboxSelect>>', select)

window.mainloop()
