# herencia

Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/herencia)
https://github.com/lauralardies/herencia

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
