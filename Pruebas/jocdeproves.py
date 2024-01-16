cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
48, 49, 50, 51, 52]

semilla = input("Agrega una semilla")


semilla = (semilla * 793 + 2323) % 23


for i in range(len(cartas) - 1, 0, -1):
	j = semilla() % (1 + 1)
	cartas[i], cartas[j] = cartas[j], cartas[1]

print(cartas)
