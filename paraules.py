SEPARADORES = (".", ",", ";", ":")

texto = input(IntroduceTexto:)
for caracter in SEPARADORES:
        texto = texto.replace(caracter, '')

palabras = texto.split()

palabras_sin_repetir =  set(palabras)

total_palabras = 0

for palabras in palabras_sin_repetir:
        total_palabras += palabras.count(palabra)

print(total_palabras, len(palabras))
