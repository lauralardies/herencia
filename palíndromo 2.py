#En esta misma clase Palindromo, añada un atributo que se inicializará en el constructor.
#Añada también un método test() que pruebe si el atributo de la instancia es un palíndromo. 
#Además, al destruir la instancia, muestre el atributo en mayúsculas.


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


print(Palindromo.Verificacion())