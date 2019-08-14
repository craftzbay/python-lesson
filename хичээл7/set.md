# Python set
**set нь элемент нь индексгүй, дахвардаж болохгүй өгөгдлийн цуглуулга төрөл юм**

## set тодорхойлох
myset = {"apple", "orange", "banana"}
print(myset)

## set-д элемент нэмэх
myset.add("cherry")
print(myset)

## set-д олон элемент нэмэх жишээ1
myset.update(["strawberry", "mango", "grapes"])
print(myset)

## set-д олон элемент нэмэх жишээ2
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

## set-н элементийн тоог олох
print(len(myset))

## set-с элемент устгах
myset.remove("banana")
myset.discard("banana")  # эдгээр нь адилхан устгах боловч ялгаатай
print(myset)


thisset = {"apple", "banana", "cherry"}
## Давталт ашиглах
for x in thisset:
    print(x)

## anana нь сэт дотор байгаа эсэхийг шалгаад хэвлэнэ.
print("banana" in thisset)

## set-с сүүлийн элементийг авч х-д хадгалаад устгах
x = thisset.pop()
print(x)
print(thisset)

## set-н бүх элементийг устгах
thisset.clear()
print(thisset)

## set-г устгах
del thisset
print(thisset)

## x set-н y set-д байхгүй элементүүдээр z set үүсгэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


## x set-н y set-д байхгүй элементүүдээр x set-г шинэчлэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

## set үүдэд давхардсан элементүүдээр set үүсгэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

## set үүдэд давхардсан элементүүдээр х set-г шинэчлэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

## set үүдэд давхардсан элемент байхгүй бол true, байвал false
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

## x set нь y set-н дэд set эсэхийг шалгах
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

## x set нь y set-н эх set эсэхийг шалгах
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

## set-үүдийн давхардаагүй элементүүдээр set үүсгэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


## set-үүдийн давхардаагүй элементүүдээр х set-г шинэчлэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

## set-үүдийн ялгаатай бүх элементүүдээр set үүсгэх
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
