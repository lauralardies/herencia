#Crear una clase Palindromo que contenga un método de clase esPalindromo(), 
#que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. 
#Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda.
#Se tienen en cuenta los caracteres no alfanuméricos.

class Cadenas:
    def __init__(self, cadena1):
        self.cadena1=cadena1
    
    def Palíndromo(self):
        cadena1=self.cadena1
        c,i,nom,cad,x = 0,0,'','',''
        i = len(cadena1)
        nom = cadena1.lower()
        while i != c:
            for x in nom:
                cad = x + cad
                c = c+1