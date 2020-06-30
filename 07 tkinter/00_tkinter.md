# [Tkinter](https://docs.python.org/3.5/library/tkinter.html#)

## Хэрэглэгчийн график интерфэйс

Tkinter нь энгийн график интерфейстэй программыг зохиох боломжтой болгодог. Tkinter сан нь цонхны элементүүдийг байрлуулан тэдгээрийг Tkinter үндсэн давталтад оруулдаг. Ингэснээр программ нь үзэгдэл (event) -ээр жолоодогддог болох ба хэрэглэгч цонхны элементүүдтэй харилцахад үзэгдэл үүсдэг. Үзэгдэл боловсруулахад зориулсан функцуудын тусламжтай ажилладаг.

`import tkinter` эсвэл `from tkinter import *` гэж ашиглана.

Tkinter ашиглан цонх үүсгэх

```python
from tkinter import *

window = Tk()
window.title("Гарчиг")
window.geometry("290x392")
window.resizable(0, 0)

window.mainloop()
```
