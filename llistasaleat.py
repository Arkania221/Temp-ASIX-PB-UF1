#Definir dos listas con nombres aleatorios
#Primera lista min 10n ; Segunda lista min 5n max 8n
#La semilla "cambia" cada que se usa

lista1 = []

lista2 = []

semilla =  375


while len(lista1) < 10:

	num_aleatorio = ((semilla * 5764) + 34256) % 100

	lista1.append(num_aleatorio)

	semilla = num_aleatorio


print(lista1)
print(lista2)
