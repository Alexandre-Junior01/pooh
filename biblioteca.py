class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
            print(f"{self.nome} foi comer")


class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"{self.nome}  é isso aí...")


class Cachorro(Animal):
    def __int__(self, nome, cor):
        super().__int__(nome, cor)

    def latir(self):
        print(f"{self.nome}, Auauauau")


class Vaca(Animal):
    def __int__(self, nome, cor):
        super().__int__(nome, cor)

    def mou(self):
        print(f"{self.nome}, Moooou")

    def comer(self):
        print(f"{self.nome}, foi comer capim")


class Coelho(Animal):
    def __int__(self, nome, cor):
        super().__int__(nome, cor)

    def pular(self):
        print(f"{self.nome}, Pula e Vive")



class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def imprimirValor(self):
        print(f" O valor do seu ingresso{self.valor}")



class Vip(Ingresso):
    def __init__(self, valor):
      super().__init__(valor * 1.5)
    def imprimirValor(self):
        print(f" O valor do seu ingresso{self.valor}")


