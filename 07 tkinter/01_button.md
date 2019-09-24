## Button - Товчлуур

`w = Button ( master, option=value, ... )`

* master - эцэг цонх
* option - Тохиргоо болон утгуудыг өгнө

Товчлуур үүсгэх жишээ

```
from tkinter import *

window = Tk()
window.title("Гарчиг")
window.geometry("290x392")
window.resizable(0, 0)


def hello():
    print('Hello Python', 'Hello Python')


B = Button(window, text="Hello", command=hello)
B.pack()

window.mainloop()
```

### Товчлуурын тохиргоонууд

1. activebackground - товчлуур дээр kурсор байгаа үед арын өнгө
2. activeforeground - товчлуур дээр kурсор байгаа үед арын өнгө
3. bd - хүрээнийн өнгө
4. bg - арын өнгө
5. command - дарсан үед ажиллах функц
6. fg - бичвэрийн өнгө
7. font - бичвэрийн фонт
8.	height - өндөр
9.	highlightcolor - фокуслах үеийн өнгө
10.	image - зураг
11.	justify -  LEFT, CENTER, RIGHT.
12.	padx - хэвтээ тэнхлэгийн зай.
13.	pady - босоо тэнхлэгийн зай.
15.	state - төлөв DISABLED, ACTIVE, NORMAL.
17.	width - өргөн