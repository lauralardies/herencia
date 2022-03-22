#En esta misma clase Palindromo, añada un atributo que se inicializará en el constructor.
#Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. 
#Además, al destruir la instancia, muestre el atributo en mayúsculas.


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