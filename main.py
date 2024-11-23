stroka = input("Введите строку: ")
stroka1 = input("Введите строку: ")
stroka2 = input("Введите строку: ")
if len(stroka) == 0 or len(stroka1) == 0 or len(stroka2) == 0:
    print("Строка введена неверно")
else:
    print (len(stroka.split()))
    print (len(stroka1.split()))
    print (len(stroka2.split()))
