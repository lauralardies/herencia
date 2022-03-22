class Test:
    def __init__(self) -> None: # Inicializamos un contador y avisamos que comienza a contar, imprimiendo en mensaje "Start log"
        self.contador = 0
        print("--Start log--")

    def __del__(self): # Al final del código esta función se ejecuta automáticamente y avisa que deja de contar las llamadas mostrando el mensaje "End log". Además indica cuántas llamadas se han contado.
        print("--End log: " + str(self.contador) + " log(s)--")
    
    def llamada(self, mensaje): # Esta función aumenta el contador cada vez que entra una llamada.
        self.contador = self.contador + 1
        print(mensaje)