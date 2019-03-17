import sys

length = int(input("Введите значение  стороны: "))
breadth = int(input("Введите значение второй стороны: "))


redeemerOrSquare = input("Что вы хотите найти Площадь или Пириметр?(S/P): ")

if redeemerOrSquare == "S" and "s":
    area = length * breadth
    print("Площадь равна: ", area)

if redeemerOrSquare == "P" or "p":
    print("Пириметр равен: " ,  2 *  (length + breadth))

