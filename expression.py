import sys

length = int(input("Введите длину: "))
breadth = int(input("Введите ширину: "))


redeemerOrSquare = input("Что вы хотите найти Площадь или Пириметр?(S/P): ")

if redeemerOrSquare == "S" and "s":
    area = length * breadth
    print("Площадь равна: ", area)

if redeemerOrSquare == "P" or "p":
    print("Пириметр равен: " ,  2 *  (length + breadth))

