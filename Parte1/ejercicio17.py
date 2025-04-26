amigos = ["Ana", "Monica", "Jose", "Camila", "Raquel", "Matias"]

"""
1. Devuelve la posicion (el index, un numero) del amigo "Matias"
2. Devuelve la misma lista pero añadiendo los amigos de la infancia
  "Ivana"  "Andres" como otra lista.
3. Agrega un nuevo amigo "Maria" devuelve el nro de amigos.
4. Elimina el ultimo elemento amigo y devuelve el nombre del amigo eliminado
5. Devuelve un arreglo ordenado alfabeticamente.

"""

# Posicion del amigo Matias
posicion = amigos.index("Matias")
print(posicion)

# Añadiendo Amigos de la infancia
amigos_infancia = ["Ivana", "Andres"]
amigos.extend(amigos_infancia)
print(amigos)

# Añadiendo a Maria y retornando el numero de amigos
amigos.append("Maria")
print(f"Los amigos totales son: {len(amigos)-1}")

# Eliminando el ultimo amigo
amgigo_eliminado = amigos.pop()
print(f"Has eliminado a: {amgigo_eliminado}")

#Lista ordenada alfabaticamente
amigos.sort()
print(f"Amigos ordenados alfabeticamente : {amigos}")
