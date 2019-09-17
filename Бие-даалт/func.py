import json
import json
def menuGarga():
    print('Цэс')
    print('----------------------------')
    print("1. Мэдээлэл харах")
    print("2. Мэдээлэл хайх")
    print("3. Мэдээлэл бүртгэх")
    print("4. Мэдээлэл устгах")
    print("5. Мэдээлэл засварлах")
    print("6. Гарах")
    print('----------------------------')
    
    f = open("data.txt","rt")
    data = f.read() # json => dict
    data = json.loads(data) # load
    
    too = inputNumber()
    if too == 1: 
        infoData(data)
    elif too == 2:
        searchData(data)
    elif too == 3:
        registerData(data)
    elif too == 6:
        f.close()
        print("Programaas garlaa!")

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
    print('Хайх цэс')
    print('----------------------------')
    print("1. Нэрээр хайх")
    print("2. Утасны дугаараар хайх")
    print("3. Буцах")
    print("4. Гарах")
    print('----------------------------')
    n = int(input())
    if n==1:
        ner = input("Хайх нэр оруулах: ")
        for i in data:
            if ner.lower() in i["ner"].lower():
                print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])
            else:
                print("Мэдээлэл олдсонгүй! ")
                break
    elif n==2:
        utas = input("Утасны дугаар оруулна уу:")
        for i in data:
            if utas in i["utas"]:
                print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])
            else:
                print("Мэдээлэл олдсонгүй! ")
                break
    elif n==3:
        menuGarga()
