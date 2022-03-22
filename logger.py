class Test:
    def __init__(self) -> None:
        self.contador = 0
        print("--Start log--")

    def __del__(self):
        print("--End log: " + str(self.contador) + " log(s)--")
    
    def llamada(self, mensaje):
        self.contador = self.contador + 1
        print(mensaje)