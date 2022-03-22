# herencia

Ejercicio 3:
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
```
