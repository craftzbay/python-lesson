import json

def menuGarga():
    print('Цэс')
    print('------------------------------')
    print("|    1. Мэдээлэл харах       |")
    print("|    2. Мэдээлэл хайх        |")
    print("|    3. Мэдээлэл бүртгэх     |")
    print("|    4. Мэдээлэл устгах      |")
    print("|    5. Мэдээлэл засварлах   |")
    print("|    6. Гарах                |")
    print('------------------------------')
    
    too = int(input())
    if too == 1:        infoData()
    elif too == 2:      searchData()
    elif too == 3:      registerData()
    elif too == 4:      deleteData()
    elif too == 5:      updateData()
    elif too == 6:      print("Programaas garlaa!")

def infoData():
    f = open("data.txt","rt")
    data = f.read()
    data = json.loads(data) # str => list
    for i in data:
        print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])
    f.close()
    menuGarga()

def registerData():
    f = open("data.txt","rt")
    data = f.read()
    data = json.loads(data) # str => list
    owog = input("Owog:")
    ner = input("Ner:")
    nas = input("Nas:")
    huis = input("Huis:")
    utas = input("Utas:")
    last = len(data)
    person = {
        "id": last,
        "owog": owog,
        "ner": ner,
        "nas": nas,
        "huis": huis,
        "utas": utas
    }
    data.append(person)
    data = json.dumps(data) # list => str
    f = open("data.txt","w")
    f.write(data)
    f.close()
    print("Амжилттай бүртгэгдлээ")
    menuGarga()

def searchData():
    f = open("data.txt","rt")
    data = f.read()
    data = json.loads(data) # str => list
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
        menuGarga()
    elif n==2:
        utas = input("Утасны дугаар оруулна уу:")
        for i in data:
            if utas in i["utas"]:
                print(i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])
            else:
                print("Мэдээлэл олдсонгүй! ")
            break
        menuGarga()
    elif n==3:
        f.close()
        menuGarga()
    else:
        print('Программаас гарлаа')
    f.close()

def deleteData():
    f = open("data.txt","rt")
    data = f.read()
    data = json.loads(data)
    f.close()
    ner = input("Мэдээллийг устгах хүний нэр оруулна уу: \n")
    for i in data:
        if ner == i["ner"]:
            print(i["id"],i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])

    id = int(input("Устгах мэдээллийн дугаарыг оруулна уу: \n"))
    data.pop(id)
    j = 0
    for i in data:
        i["id"] = j
        j+=1
    data = json.dumps(data)
    f = open("data.txt","w")
    f.write(data)
    f.close()
    print("Мэдээлэл устлаа\n\n")

    menuGarga()

def updateData():
    f = open("data.txt","rt")
    data = f.read()
    data = json.loads(data)
    f.close()
    ner = input("Нэр оруулна уу:\n")
    for i in data:
        if ner.lower() == i["ner"].lower():
            print(i["id"],i["owog"],i["ner"],i["nas"],i["huis"],i["utas"])

    id = int(input("Засварлах мэдээллийн дугаарыг оруулна уу: \n"))
    
    data[id]["owog"] = input("Овог оруулна уу:")
    data[id]["ner"] = input("Нэр оруулна уу:")
    data[id]["nas"] = input("Нас оруулна уу:")
    data[id]["huis"] = input("Хүйс оруулна уу:")
    data[id]["utas"] = input("Утас оруулна уу:")

    f = open("data.txt","w")
    data = json.dumps(data)
    f.write(data)
    f.close()
    print("Амжилттай засварлалаа\n\n")
    menuGarga()






