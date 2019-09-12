import json
import func
f = open("data.txt","rt")
data = f.read() # json => dict
data = json.loads(data) # load

func.menuGarga()
too = func.inputNumber()

# control + \

if too == 1: 
    func.infoData(data)
elif too == 2:
    func.searchData(data)
elif too == 3:
    func.registerData(data)
elif too == 7:
    f.close()
    print("Programaas garlaa!")
