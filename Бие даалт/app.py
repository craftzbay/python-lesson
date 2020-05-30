from function import showMenu, create, remove

showMenu()

n = int(input('Үйдлийн дугаар оруулна уу: '))

if n == 1:
    print('Та өөр дугаар оруулна уу энэ үйлдэл гэрийн даалгавар')
elif n == 2:
    create()
elif n == 3:
    remove()
elif n == 4:
    print('Та өөр дугаар оруулна уу энэ үйлдэл гэрийн даалгавар')
else:
    print('Та программаас гарлаа...')
