## CheckButton - Сонгох товчлуур 

from tkinter import *

window = Tk()
window.title("Гарчиг")
window.geometry("290x392")
window.resizable(0, 0)


B = Checkbutton(window, text="Video", variable='1',
                onvalue=1, offvalue=0, height=5,  width=20)
B.pack()

window.mainloop()
