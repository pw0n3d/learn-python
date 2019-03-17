import sys

print("\t\t***Cложение/Вычитание/Умножение/Деление***\n")


number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число:  "))


act = input("Эти числа нужно сложить или вычесть?(- + * /): ")

if act == "-":
    actResult = number1 - number2
    print(number1 , "-" ,number2 ,"=" ,actResult)

if act == "+":
    actResult = number1 + number2
    print(number1 , "+" ,number2 ,"=" ,actResult)

if act == "*":
    actResult = number1 * number2
    print(number1 , "*" ,number2 ,"=" ,actResult)

if act == "/":
    actResult = number1 / number2
    print(number1 , "/" ,number2 ,"=" ,actResult)

print("\t\t***Возведение в степень***\n")


num1 = float(input("Введите число которое нужно возвести в степень: "))
powerNum = float(input("Введите в какую степерь нужно возвести число: "))

result = num1 ** powerNum

print(num1 , "**" , powerNum , " = " , result )


print("\t\t***Возвращение не полное частное число от деления***\n")


inputNum1 = int(input("Введите первое число: "))
inputNum2 = int(input("Введите второе число: "))

remainder = inputNum1 // inputNum2

print(inputNum1 , '''//''' , inputNum2 ,"=" ,remainder )


print("\t\t***Возвращение остаток от деления***\n")

divider = int(input("Введите первое число: "))
dividend = int(input("Введите второе число: "))

output = divider % dividend

print(divider , "%" , dividend , "=" , output)

print("\t\t***Сдвиги в лево/право***\n")

slideInfo = input("В какую сторону будет сдвиг?( << / >> ) ")
slideNum = int(input("Введите число: "))
slideOperatioNum = int(input("На сколько значений нужно сделать сдвиг: "))

if slideInfo == "<<":
    slideResult = slideNum << slideOperatioNum
    print( slideNum , "<<" , slideOperatioNum , "=" ,slideResult)

if slideInfo == ">>":
    slideResult = slideNum >> slideOperatioNum
    print( slideNum , ">>" , slideOperatioNum , "=" ,slideResult)
