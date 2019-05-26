N = int(input())
sum = 0


for i in range(1, N + 1 ):
	if (i % 3 == 0):
        	sum += i

print("Сумма натуральных чисел равно = ", sum )
