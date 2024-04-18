class Animal:
    def __init__(self,nome):
        self.nome = nome

    def som(self):
        print("o animal faz algum som")

class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome)
        self.raça = raça

    def som(self):
        print("o cachorro faz au au")

animal_generico = Animal("animal")
animal_generico.som()

cachorro1 = Cachorro("Rex", "Labrador")

animal_generico.som()
cachorro1.som()