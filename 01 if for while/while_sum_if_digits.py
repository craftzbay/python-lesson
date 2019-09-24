# а аас б хүртэлх тооноос цифрүүдийн нийлбэр нь к байх тоонуудыг олох

a = int(input())
b = int(input())
k = int(input())
c = max(a, b)

# нөхцөлт давталт
while c >= min(a, b):
    # с тооны цифрүүдийн нийлбэр олох // 123 => 1 + 2 + 3 = 6
    i = sum(int(j) for j in str(c))
    # нөхцөл шалгах
    if i == k:
        print(c)
    c -= 1
