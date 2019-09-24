"""
@ Гараас утга оруулах
"""

# Тоо гараас авах үед төрөл хөрвүүлж байхыг анхаарах
x = input("х тоо: ")
y = input("y тоо: ")
z = int(x) + int(y)

print("x тоо: " + x)
print("y тоо: " + y)
print("x + y = " + str(z))

# Тэмдэгт мөр гараас авах
ner = input("Нэр оруулна уу: ")
print("Сайн байна уу " + ner)
nas = ("Та хэдэн настай вэ? ")
print("Нэр: " + ner + " , " + "Нас: " + nas)


"""
@ нэг мөрөс олон хувьсагчид утга авах
"""
# Python 3
var1, var2 = [int(x) for x in input().split()]
print(var1 + var2)
# Python 2
var1, var2 = [int(x) for x in raw_input().split()]
print(var1 + var2)
