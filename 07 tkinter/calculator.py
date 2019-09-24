from tkinter import *

window = Tk()
window.title("Calculator UI")
window.geometry("290x392")
window.resizable(0, 0)

# хувьсагчид
ilerhiilel = ""
result_string = StringVar()


# товчлуур дарах үе утга авах функц
def btn_click(item):
    global ilerhiilel
    ilerhiilel = ilerhiilel + str(item)
    result_string.set(ilerhiilel)


# устгах товч дарах үед илэрхийллийг хоосон болгох
def btn_clear():
    global ilerhiilel
    ilerhiilel = ""
    result_string.set("")


# Үр дүн болон илэрхийлэл харуулах хэсэг
top_frame = Frame(window, width=290, height=50, bg="#F19748", bd=0)
top_frame.pack(side=TOP, padx=0, pady=0)

# үр дүн харуулах input
result = Entry(top_frame, font=('arial', 18, 'bold'),
               bd=0, bg="#F19748", width=50, justify=RIGHT,
               textvariable=result_string)
result.grid(row=0, column=0)
result.pack(pady=35, padx=30)

# товчлууруудын хэсэг
btns_frame = Frame(window, width=290, height=282.5, bg="", bd=0)
btns_frame.pack()

ce = Button(btns_frame, command=lambda: btn_clear(), font=("arial", 10), text="CE", width=26, height=3, fg="black",
            bg="#EAEAEA", bd=0,  cursor="hand2").grid(row=0, column=0, columnspan=3, padx=1, pady=1)
urjih = Button(btns_frame, command=lambda: btn_click("*"), font=("arial", 10), text="x", width=8, height=3, fg="black",
               bg="#EAEAEA", bd=0,  cursor="hand2").grid(row=0, column=3, padx=1, pady=1)
doloo = Button(btns_frame, command=lambda: btn_click(7), font=("arial", 10), text="7", width=8, height=3, fg="black",
               bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
naim = Button(btns_frame, command=lambda: btn_click(8), font=("arial", 10), text="8", width=8, height=3, fg="black",
              bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
yes = Button(btns_frame, command=lambda: btn_click(9), font=("arial", 10), text="9", width=8, height=3, fg="black",
             bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
huwaah = Button(btns_frame, command=lambda: btn_click("/"), font=("arial", 10), text="/", width=8, height=3, fg="black",
                bg="#EAEAEA", bd=0,  cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
dorow = Button(btns_frame, command=lambda: btn_click(4), font=("arial", 10), text="4", width=8, height=3, fg="black",
               bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
taw = Button(btns_frame, command=lambda: btn_click(5), font=("arial", 10), text="5", width=8, height=3, fg="black",
             bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
zurgaa = Button(btns_frame, command=lambda: btn_click(6), font=("arial", 10), text="6", width=8, height=3, fg="black",
                bg="#F5F5F5", bd=0,  cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
hasah = Button(btns_frame, command=lambda: btn_click("-"), font=("arial", 10), text="-", width=8, height=3, fg="black",
               bg="#EAEAEA", bd=0,  cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
neg = Button(btns_frame, command=lambda: btn_click(1), font=("arial", 10), text="1", width=8, height=3, fg="black",
             bg="#F5F5F5", bd=0, cursor="hand2").grid(row=3, column=0, padx=0, pady=0)
hoyr = Button(btns_frame, command=lambda: btn_click(2), font=("arial", 10), text="2", width=8, height=3, fg="black",
              bg="#F5F5F5", bd=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
guraw = Button(btns_frame, command=lambda: btn_click(3), font=("arial", 10), text="3", width=8, height=3, fg="black",
               bg="#F5F5F5", bd=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
nemeh = Button(btns_frame, command=lambda: btn_click("+"), font=("arial", 10), text="+", width=8, height=3, fg="black",
               bg="#EAEAEA", bd=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
teg = Button(btns_frame, command=lambda: btn_click(0), font=("arial", 10), text="0", width=17, height=3, fg="black", bg="#F5F5F5",
             bd=0, cursor="hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tseg = Button(btns_frame, command=lambda: btn_click("."), font=("arial", 10), text=".", width=8, height=3, fg="black", bg="#F5F5F5",
              bd=0, cursor="hand2").grid(row=4, column=2, padx=1, pady=1)
tentsuu = Button(btns_frame, font=("arial", 10), text="=", width=8, height=3, fg="black", bg="#EAEAEA",
                 bd=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

window.mainloop()

# EAEAEA
# F5F5F5
