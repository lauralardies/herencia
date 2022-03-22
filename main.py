# En este archivo importamos las clases que vamos a usar.
from puzle import A 
from logger import Test
from palíndromo import Cadenas
from palíndromo_2 import Palindromo

# Ejercicio 1:
print("Ejercicio 1:\n")

cadena1 = input("Dame una palabra: ")
op1 = Cadenas(cadena1)

print(op1.Palindromo())

# Ejercicio 2:
print("\nEjercicio 2:\n")

cadena1= input("Dame una palabra: ")
palindromo = Palindromo(cadena1)

print(palindromo.Verificacion())

# p = Palindromo("radar") 
# print(p.test()) 
# >>> True 
# p = Palindromo("sonar") 
# >>> RADAR 
# print(p.test()) 
# >>> False 
# SONAR 

# ¿Por qué se muestra RADAR después de la instanciación Palindromo("sonar")?

# La respuesta se encuentra en el enunciado del ejercicio. Hay una frase que dice lo siguiente : 
# "al destruir la instancia, muestre el atributo en mayúsculas". Esto es lo que pasa, a la instancia p se le asigna un valor nuevo, 
# es decir, se destruye la instancia p de RADAR para cambiarlo por una misma instancia p de SONAR. Como se destruye la instancia de
# RADAR, entonces se imprime el atributo RADAR en mayúsculas.

# Ejercicio 3
print("\nEjercicio 3:\n")

a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

# Podemos ver que los mensajes que se muestran son:
# >>> <class 'puzle.A'>
# >>> False
# >>> 0
# >>> 1
# >>> 2
# >>> 3

# Ejercicio 4:
print("\nEjercicio 4:\n")

test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada(str(i) + "ª llamada") 