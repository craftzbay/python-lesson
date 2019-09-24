## Тэмдэгт мөртэй ажиллах функцууд
1. Эхний тэмдэгт том болгох
```
txt = "сайн уу"
x = txt.capitalize()
print (x)
```
2. Бүх тэмдэгтийг жижиг болгох (lower, casefold)
```
txt = "Сайн Байна уу!"
x = txt.casefold()
print (x)
```
3. Тэмдэгт мөрийг тэмдэгтүүдийн голд байрлуулах
```
txt = "Сайн уу"
x = txt.center(20, "p")
print(x)
```
4. Тэмдэгт мөрөөс тэмдэгт мөр тоолох /**string.count(value, start, end)**/
```
txt = "Сайн байна уу, Пайтон хичээл орох гэж байна"
x = txt.count("байна")
print(x)
```
5. Тэмдэгт мөрөөс хайж байрлалыг буцаана
```
txt = "Сайн уу, хичээлд тавтай морил."
x = txt.find("хичээл")
print(x)
```
6. Тэмдэг мөрийг хэвжүүлэх
```
txt = "Зөвхөн {үнэ:.2f} төгрөг!"
print(txt.format(үнэ = 50))
```
7. Индэксийг олох
```
txt = "Сайн уу, хичээлд тавтай морил."
x = txt.index("хичээл")
print(x)
```
8. Тэмдэгт мөр нь бүгд цифр эсэхийг шалгах
```
txt = "50800"
x = txt.isdigit()
print(x)
```
9. Бүх тэмдэгт жижиг эсэхийг шалгах
```
txt = "hello world!"
x = txt.islower()
print(x)
```
10. Бүх тэмдэгт тоо эсэхийг шалгана
```
txt = "565543"

x = txt.isnumeric()

print(x)
```
11. Бүх тэмдэгт хоосон зай эсэхийг шалгана
```
txt = "   "

x = txt.isspace()

print(x)
```
12. Тэмдэгт мөрийн эхний үсгүүд том эсэхийг шалгана
```
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)
```
13. Тэмдэгт мөрийн бүх үсэг том эсэхийг шалгана
```
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)
```
14. Элементүүдийг холбон тэмдэгт мөр үүсгэх
```
myTuple = ("Сайн", "байна", "уу")

x = "#".join(myTuple)

print(x)

```
15. Зүүн талаас нь тэгээр дүүргэх
```
txt = "50"

x = txt.zfill(10)

print(x)
```
16. Зүүн талаас хоосон зай устгах
```
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
```
17. Хэсгүүдэд хуваах
```
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
```
18. Дарж солих
```
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)
```
19. Баруун талаас хайж байрлалыг буцаана **rindex**
```
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)
```
20. Тэмдэгт мөрийг хуваах
```
txt = "welcome to the jungle"

x = txt.split()

print(x)
```
21. Тэмдэгт мөрийг мөрөөр хуваах
```
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)
```
22. Тэмдэгт мөр юугаар эхэлсэнийг шалгах
```
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)
```
23. Хоосон зайг устгах
```
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")
```
24. Том тэмдэгтийг жижиг, том тэмдэгтийг том болгох
```
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)
```
25. Тэмдэгт мөрийг гарчиг болгох
```
txt = "Welcome to my world"

x = txt.title()

print(x)
```
