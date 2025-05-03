""" 
Signo Zodiacal

El signo zodiacal de una persona está determinado por su dia
de nacimiento.

El diccionario de signos asocia a cada signo el periodo del año
que le corresponde. Cada periodo es una tupla con la fecha de inicio
y la fecha de termino, y cada fecha es una tupla(mes, dia)

signos = {
  
  "aries": ((3,21),(4,20))
  "tauro": ((4,21),(5,21))
  "geminis": ((5,22),(6,21))
  "cancer": ((6,22),(7,23))
  "leo": ((7,24),(8,23))
  "virgo": ((8,24),(9,23))
  "libra": ((9,24),(10,23))
  "escorpio": ((10,24),(11,22))
  "sagitario": ((11,23),(12,21))
  "capricornio": ((12,22),(1,20))
  "acuario": ((1,21),(2,19))
  "piscis" :((2,20)(3,20))
  
}

Pro ejemplo para que una persona sea de signo libra debe haber nacido 
entre el 24 de septiembre y el 23 de octubre.

Escriba la fucnion determinar_signo(fecha_de_nacimiento) que reciba como
parametro la fecha de nacimiento de una persona, representada
como una tupla(año, mes, dia)y que retorne el signo zodiacal de la persona

determinar_signo((1990,5,7))
tauro

"""