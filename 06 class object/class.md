# Класс, Обьект
## Обьект хандалтад программчлалын тухай

Класс (class-анги) нь өгөгдөл болон функцуудаас тогтох өгөгдлийн хийсвэр төрөл юм. Бидний өмнө үзсэн цуглуулга (collection) төрөлтэй төстэй
боловч өгөгдөлд хандах хандалт нь ялгаатай байдгаараа онцлогтой юм. Цуглуулга төрлийн өгөгдлийн талбарт хандах хандалт нээлттэй байдаг бол
классын талбарт хандах хандалтыг хязгаарлаж болдог. Үүнийг өгөгдлийн далдлалт буюу өгөгдлийн битүүмжлэл гэдэг.

1. Класс тодорхойлох
MyClass гэсэн нэртэй классыг x=5 бүхий гишүүн өгөгдөлтэй тодорхойлж классын p1 обьектоор дамжуулан гишүүн өгөгдөлийн утгыг хэвлэж байна
```
class MyClass:    # класс зарлах
  x = 5           # Гишүүн өгөгдөл
p1 = MyClass()    # Классын обьекь зарлах
print(p1.x)       
```
2. Байгуулагч функц 
Python хэлд классын байгуулагч функцийг __init__() гэж тодорхойлсон байдаг.Шинэ обьект үүсгэхэд класс ашиглагдах бүрт байгуулагч функц автоматаар ажилладаг. Байгуулагч функц нь классын гишүүн өгөгдөлд утга оноох үүрэгтэй. Доорх жишээг
тайлбарлавал: Person класс нь name, age гэсэн гишүүн өгөгдөлтэй ба байгуулагч функцээр дамжуулан утга оноож өгч байна.
```
class Person:
  def __init__(self, name, age):  # Байгуулагч функц
    self.name = name
    self.age = age

p1 = Person("John", 36)      # Person классын байгуулагч функц ашиглан обьект үүсгэх

print(p1.name)
print(p1.age)
```
3. self параметр
self параметр нь тухайн классын өгөгдөлт хандахад ашиглагддаг. Энэ нь заавал self нэртэй байх албагүй ба классын аль ч функцийн эхний параметр байх ёстой
```
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

```
4. Гишүүн функц
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):           # Гишүүн функц тодорхойлох
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```
5. Гишүүн өгөгдөлийн утгыг өөрчлөх
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)
```
6. Гишүүн өгөгдөл устгах
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)
```
7. Классын обьект устгах
```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)
```
