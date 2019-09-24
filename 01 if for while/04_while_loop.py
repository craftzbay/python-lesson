# for loop: a аас b хүртэлх бүх тоог хэвлэх
a, b = input().split()
c = max(a, b)
d = min(a, b)

while d <= c:
    print(d)
    d += 1
