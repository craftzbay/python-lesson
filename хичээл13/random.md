## Дурын тоо үүсгэх болон дурын элемент сонгох зарим функцууд
1. Санамсаргүй бутархай тоо үүсгэх
```
import random
print(random.uniform(20, 60))
```
2. 0 - ээс 1 - ийн хооронд санамсаргүй тоо үүсгэх
```
import random

print(random.random())
```
3. Дурын k элементүүдээр жагсаалт үүсгэх
```
import random

mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))
```
4. Элементүүдийн байрыг санамсаргүй байрлалаар өөрчлөх
```
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)
```
5. Санамсаргүй элемент сонгох
```
import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))
```
