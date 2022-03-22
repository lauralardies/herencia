#Crear una clase Palindromo que contenga un método de clase esPalindromo(), 
#que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. 
#Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda.
#Se tienen en cuenta los caracteres no alfanuméricos.

class Cadenas:
    def __init__(self, cadena):
        self.cadena=cadena
    
    def Palíndromo(self):
        cadena=self.cadena