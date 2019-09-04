# Python tuple
## tuple нь эрэмбэлэх боломжгүй, элемент давхардаж болох ч элемент өөрчлөх боломжгүй өгөгдлийн цуглуулгын төрөл юм
## tuple үүсгэх
mytuple = ("apple", "banana", "cherry")

## tuple хэвлэх
print(mytuple)

## индексээр хэвлэх
print(mytuple[1])

## tuple-ийн урт буюу элементүүдийн тоог хэвлэх
print(len(mytuple))

## tuple-д "banana" хэд байгааг тоолох
x = mytuple.count("banana")
print(x)

## "cherry" - н индексийг олох
y = mytuple.index("cherry")
print(y)

## for
for x in mytuple:
    print(x)

## if
if "cherry" in mytuple:
    print("yes")

## tuple устгах
del mytuple
