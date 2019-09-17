import func

username = input("Хэрэглэгчийн нэр: ")
password = input("Нууц үг: ")
if username == 'admin' and password == 'password':
    func.menuGarga()
else:
    print('Хэрэглэгчийн нэр, нууц үг буруу байна! ')
