# a болон b тооны үржвэрийг давталтаар олох
# 3*5 = 3+3+3+3+3

a = int(input("a: "))
b = int(input("b: "))

niilber = 0
for i in range(1, b+1):
    niilber = niilber + a
print(niilber)
