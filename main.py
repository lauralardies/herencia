# En este archivo importamos las clases que vamos a usar.
from puzle import A 
from logger import Test

# Ejercicio 1:
print("Ejercicio 1:\n")

from palíndromo import Cadenas

cadena1 = input("Dame una palabra: ")
op1 = Cadenas(cadena1)

print(op1.Palindromo())

# Ejercicio 2:
print("\nEjercicio 2:\n")

from palíndromo_2 import Palindromo

cadena1= input("Dame una palabra: ")
palindromo = Palindromo(cadena1)

print(palindromo.Verificacion())

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