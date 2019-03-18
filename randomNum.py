import random

print("\t\t***Игра угадай число***")
print("У тебя есть 5 попыток \nПопытайся угадать секретное.\nУдачи!")

attemps = 0
secretNum = random.randint(0 , 10)

while True:
    magician = int(input("Введите секретное число:"))

    attemps = attemps + 1

    if attemps == 5:
        print("Ты проиграл\nУ тебя закончились попытки")
        break

    if magician == secretNum:
        print("\t\tПоздравляю вы угадали!!!")
        print(secretNum)
        break

    if magician < secretNum:
        print("Нет , секретное число больше этого ")

    if magician > secretNum:
        print("Нет , меньше этого")
