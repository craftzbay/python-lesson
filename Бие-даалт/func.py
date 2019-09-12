import json
def menuGarga():
    print("1. Мэдээлэл харах")
    print("2. Мэдээлэл хайх")
    print("3. Мэдээлэл бүртгэх")
    print("4. Мэдээлэл устгах")
    print("5. Мэдээлэл засварлах")
    print("6. Буцах")
    print("7. Гарах")

def inputNumber():
    return int(input())

def infoData(data): # list
    for i in data:
        print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])

def registerData(data): # list
    owog = input("Owog:")
    ner = input("Ner:")
    nas = input("Nas:")
    huis = input("Huis:")
    utas = input("Utas:")

    person = {
        "owog": owog,
        "ner": ner,
        "nas": nas,
        "huis": huis,
        "utas": utas
    }
    data.append(person)
    data = json.dumps(data) # dict => str
    f = open("data.txt","w")
    f.write(data)
    f.close()
    print("Амжилттай бүртгэгдлээ")

def searchData(data):
    ner = input("Хайх нэр оруулах: ")
    for i in data:
        if ner.lower() in i["ner"].lower():
           print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])
        else:
           print("Мэдээлэл олдсонгүй! ")
           break
