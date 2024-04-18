class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self):
        print(f"o {self.modelo} está acelerando")

    def freiar(self):
        print(f"o {self.modelo} freiou")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def AbrirPorta(self):
        print(f"porta aberta do {self.modelo}")
    
class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def Empinar(self):
        print(f"a moto {self.modelo} está empinando")

if __name__ == "__main__":
    carro1 = Carro("Ford", "Ka")
    moto1 = Moto("Honda", "151")

carro1.acelerar()
carro1.freiar()
carro1.AbrirPorta()

moto1.acelerar()
moto1.Empinar()