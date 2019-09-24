# Гурван оронтой бүх палендром тоог олж тоолох
c = 0
for i in range(100, 200):
    a = i // 100
    b = i % 10
    if a == b:
        c = c + 1
        print(i)
print("niit: ", c)
