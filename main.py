class Cuadrado:
    def __init__(self, tamaño):

        self.tamaño = tamaño

    def dibujar(self):

        for i in range(self.tamaño):
            for j in range(self.tamaño):

                if i == 0 or i == self.tamaño - 1 or j == 0 or j == self.tamaño - 1:
                    print("*", end=" ")
                else:

                    print(" ", end=" ")

            print()


tamaño = int(input("Ingrese el número de asteriscos por lado del cuadrado: "))

cuadrado = Cuadrado(tamaño)

cuadrado.dibujar()
