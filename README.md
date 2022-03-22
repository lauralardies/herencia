# herencia

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/herencia)
https://github.com/lauralardies/herencia

Ejercicio 1: En este ejercicio pide crear una clase que identifique si una palabra es o no palíndromo.
```
class Cadenas:
    def __init__(self, cadena1):
        self.cadena1=cadena1
    
    def Palindromo(self):
        cadena1=self.cadena1
        c,i,nom,cad,x = 0,0,'','',''
        i = len(cadena1)
        nom = cadena1.lower()
        while i != c:
            for x in nom:
                cad = x + cad
                c = c+1
            if nom == cad:
                return str("True")
            else:
                return str("False")

cadena1 = input("Dame una palabra: ")
op1 = Cadenas(cadena1)

print(op1.Palindromo())
```
Ejercicio 2: En este ejercicio pide crear un atributo que se inicializará en el constructor, verificar si la instancia es un palíndromo y que muestre el atributo en mayúsculas.

```
class Palindromo:
    def __init__(self, cadena1):
        self.cadena1=cadena1
    
    def Verificacion(self):
        cadena1= input("Dame una palabra: ")
        print(cadena1.upper())
        if cadena1 == ''.join(reversed(cadena1)):
            return str("True")
        else:
            return str("False")
            
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
```

Ejercicio 3: En este ejercicio se pide decir qué es lo que muestra el mensaje del siguiente código. La respuesta está en el mismo código.
```
class A: 
    def z(self): # Devuelve la clase.
        return self 
 
    def y(self, t): # Devuelve la longitud de un parámentro t (puede ser lista, string... Lo que sea)
        return len(t) 
        
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
```

Ejercicio 4: Este ejercicio te pide crear una clase Logger en la cual se cuenten las llamadas que entran, almacenandolas en una variable. 
```
class Test:
    def __init__(self) -> None: # Inicializamos un contador y avisamos que comienza a contar, imprimiendo en mensaje "Start log"
        self.contador = 0
        print("--Start log--")

    def __del__(self): # Al final del código esta función se ejecuta automáticamente y avisa que deja de contar las llamadas mostrando el mensaje "End log". Además indica cuántas llamadas se han contado.
        print("--End log: " + str(self.contador) + " log(s)--")
    
    def llamada(self, mensaje): # Esta función aumenta el contador cada vez que entra una llamada.
        self.contador = self.contador + 1
        print(mensaje)
 
test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada(str(i) + "ª llamada")        
 
```
