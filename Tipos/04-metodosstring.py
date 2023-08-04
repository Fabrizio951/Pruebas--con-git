animal = "chAnchito Feliz"
animal2 =" chanchito triste "

"Convertir todo a mayuscula"

print(animal.upper())

"Convertir todo a minuscula"

print(animal.lower())

"Primer elemento mayuscula el resto minuscula"

print(animal.capitalize())

"Las primeras letras de las palabras separadas tiene mayuscula"

print(animal2.title())

"Borrar espacio de los extremos"

print(animal2.strip())

"Se pueden usar dos funciones al mismo tiempo"

print(animal2.strip().capitalize())


"Borrar espacio de la derecha"

print(animal2.rstrip())

"Borrar espacio de la izquierda"

print(animal2.lstrip())

"Buscar cadena de caracteres / si es -1 es que no existe"

print(animal.find("it"))

"Reemplazar un valor"

print(animal.replace("ch","p"))

"Devolver un boleano"

print("ch" in animal)

print("ch" not in animal)
