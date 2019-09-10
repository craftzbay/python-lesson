# Удамшил
# Python Inheritance
Нэг классаас өөр класс удимшин тухайн классын бүх гишүүн өгөгдөл болон функцуудыг өвлөн авахыг удимшил гэдэг.

***Parent class*** эцэг класс буюу үндсэн класс.

***Child class*** хүү класс буюу өөр ангиас өвлөгдөн үүссэн класс.

1. Эх класс 
Ямар ч классын хувьд эх класс болж чаддаг.
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```

2. Хүү класс
Хүү класс тодорхойлох доо дараах байдлаар бичнэ:
```
class Student(Person):
  pass
```
***pass*** түлхүүр үг нь эх классын гишүүдээс өөр өгөгдөл болон функц нэмэж тодорхойлох шаардлагагүй бол хэрэглэнэ.

3. Удамшил
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
```
Хүү класс ажиллахдаа эх классын байгуулагч функцийг ажиллуулж байна.

4. Байгуулагч функц
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()
```
- __init __ () функцийг нэмэхэд хүү класс нь эцэг классын __init __ () функцийг цаашид өвлөхгүй болно.
- Эцэг классын __init __ () функцийг хадгалахын тулд эцэг классын __init __ () функцэд дээрх байдлаар дуудлага нэмж ашиглана.

5. super() функц
Python нь super() функцтэй бөгөөд энэ нь хүү класс нь эцэг классаас бүх гишүүн өгөгдөл болон функцуудыг өвлөн авах боломжийг олгоно.
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()
```
6. Гишүүн өгөгдөл нэмэх
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
```

```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

```
7. Гишүүн функц нэмэх
```
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
```
