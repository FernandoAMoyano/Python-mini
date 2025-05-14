def mostrar_usuarios(lista):
 
    if len(lista) < 1:
      print("Aun no hay usuarios registrados, puedes hacerlo desde opcion 2")
    else:
       for i,usuario in enumerate(lista):
        print(f"Usuario {i+1}: {usuario}")
        
        

def registrar_usuario(lista, usuario):
  lista.append(usuario)
  return f"Usuario {usuario} registrado con exito!"

def eliminar_usuario(lista, usuario):
  lista.remove(usuario)
  return f"Usuario {usuario} eliminado de la lista"

def buscar_usuario(lista, usuario):
  if usuario in lista:
    return f"Usuario {usuario} encontrado"
  else:
    return f"Usuario{usuario} no encontrado"