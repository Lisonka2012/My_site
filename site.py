print("Привіт! Я МАТБОТ, я тобі допоможу з математикою")
a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a==1:
    b = float(input("1 число"))
    print("+")
    c = float(input("2 число"))
    print(b , "+" , c , "=" , b+c)
    a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a==2:
    d = float(input("1 число"))
    print("-")
    e = float(input("2 число"))
    print(d , "-" , e , "=" , d-e)
    a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a==3:
    f = float(input("1 число"))
    print("*")
    g = float(input("2 число"))
    print(f , "*" , g , "=" , f*g)
    a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a==4:
    h = float(input("1 число"))
    print("/")
    i = float(input("2 число"))
    print(h , "/" , i , "=" , h/i)
    a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a==5:
    j = float(input("1 число"))
    print("в ")
    k = float(input("2 число"))
    print(j , "в" , k , "=" , j**k)
    a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
while a == 6:
    poka=input("Ця цифра щоб вийти. Ти хочеш вийти?")
    while (poka == "так"):
        print("Було весело! Пока! :(")
        break
    while (poka == "ні"):
        print("Ураааа! Ось що я можу:")
        a=int(input("Введи операцію: 1 = +; 2 = -; 3 = *; 4 = /; 5 = степінь"))
