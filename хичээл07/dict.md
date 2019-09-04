# Python dictionary
**dictionary нь түлхүүр болон утгаас бүрдэх өвөрмөц төрөл юм.**

## dictionary тодорхойлох
```
mydictionary = {
    "owog" : "Baldan",
    "ner" : "Saraa",
    "nas" : 25
}
print(mydictionary)
```

## dictionary-н элементэд хандахаа түлхүүрээр хандана
```
n = mydictionary.['ner']
print(n)
m = mydictionary.get("ner")
print(m)
```

## for давталт ашиглах1
```
for x in mydictionary:
  print(x)
```

## for давталт ашиглах2
```
for x in mydictionary:
  print(mydictionary[x])
```

## for давталт ашиглах3
```
for x in mydictionary.values():
  print(x)
```
## for давталт ашиглах4
```
for x, y in mydictionary.items():
  print(x, y)
```

## нөхцөл шалгах
```
if "ner" in mydictionary:
  print("Нэр байна")
```

## dictionary-д элемент нэмэх
```
хүн =	{
  "нэр": "Болд",
  "овог": "Баатар",
  "нас": 26
}
хүн["хүйс"] = "эр"
print(хүн)
```

## dictionary-с элемент устгах
```
хүн.pop("хүйс")
del хүн["нас"]
print(хүн)
```

## dictionary-н бүх элементийг устгах
```
хүн.clear()
print(хүн)
```

## dictionary-г хуулбарлах
```
хүн1 = хүн.copy()
print(хүн1)
```

## Байгуулагч ашиглан үүсгэх
```
н = dict(хүн)
print(н)
```


## dictionary-үүдийн ялгаатай бүх элементүүдээр dictionary үүсгэх
```
машин = {
  "бренд": "Ford",
  "загвар": "Mustang",
  "он": 1964
}
машин.update({"өнгө": "цагаан"})
print(машин)
```
