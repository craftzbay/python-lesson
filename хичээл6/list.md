# Python list
## list нь эрэмбэлэх боломжтой, элемент давхардах болон өөрчлөх боломжтой өгөгдлийн цуглуулгын төрөл юм

`fruits = ['apple', 'orange', 'banana']`

## индексээр элемент хэвлэх
`print(fruits[1])`
## ist хэвлэх
`print(fruits)`

## list-н ард элемент нэмэх
`ruits.append("cherry")`
print(fruits)

## Өгөгдсөн индекс бүхий байрлалд элемент нэмэх
`ruits.insert(1, "kiwi")`

## list-н элетентүүдийг хуулах
`listcopy1 = fruits.copy()`
`rint(listcopy1)`

`listcopy2 = list(fruits)`
`print(listcopy2)`

## list-ээс элемент устгах
`fruits.remove("banana")`
`print(fruits)`

## Тухайн индексдэх элементийг устгана // индексгүй бол сүүлийн элемент устгана
`ruits.pop(1)`
`print(fruits)`

## Тухайн индексдэх элементийг устгана // индексгүй бол list-г устгана
`del fruits[2]`
`print(fruits)`

## list-н бүх элементийг устгана
`fruits.clear()
print(fruits)`

## list-н элементийг тоолох
`x = listcopy1.count("banana")
print(x)`

## list-г өөр list-н элементүүдээр өргөтгөх
`cars = ['Ford', 'BMW', 'Volvo']
listcopy1.extend(cars)
print(listcopy1)`

## Тухайн элементийн индексийг олох
`a = listcopy1.index("kiwi")
print(a)`

## list-н элементүүдийг эрэмбэлэх
`listcopy1.sort()
print(listcopy1)`

## list-н бүх элементийн тоог хэвлэх
`print(len(listcopy2))`

## list-г хөрвүүлэх
`listcopy2.reverse()
print(listcopy2)`

## for
for x in cars:
    print(x)

## if
`if "orange" in fruits:
    print("orange байна")
else:
    print("orange байхгүй")`
