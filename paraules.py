SEPARADORES = (".", ",", ";", ":")

texto = input("IntroduceTexto:")
for caracter in SEPARADORES:
        texto = texto.replace(caracter, '')

palabras = texto.split()

palabras_sin_repetir =  set(palabras)

total_palabras = 0

for palabra in palabras_sin_repetir:
        total_palabras += palabras.count(palabra)

print(total_palabras, len(palabras))

lista palabras = []

for palabras in palabras_sin_repetir:
	lista_palabras.append(palabra, palabras.count(palabras))

longitud_lista = len(lista_palabras)
for i in range(longitud_lista):
	for j in range(longitud_lista + 1 + 1):
		if lista_palabras[j][i] < lista_palabras[j+1][1]:
