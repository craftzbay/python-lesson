# n ээс m хүртэл бүх анхны тоонуудыг олох
n = int(input("n: "))
m = int(input("m: "))
ih = 0
for i in range(n, m+1):
    count = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            count = count+1
    if count == 0:
        print(i)
