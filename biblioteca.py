class Animal():
     def __init__(self, nome, cor):
        self.nome = nome
        self.cor=cor

        def comer(self):
         print(f"{self.nome} foi comer")


class Gato(Animal):
 def __init__(self,nome,cor):
     super().__init__(nome,cor)

 def miar(self):
     print(f"{self.nome}  é isso aí...")



class Cachorro(Animal):
    def __int__(self,nome,cor):
        super().__int__(nome,cor)

    def latir(self):
        print(f"{self.nome}, Auauauau")

class Vaca(Animal):
    def __int__(self,nome,cor):
        super().__int__(nome,cor)

    def Mou(self):
        print(f"{self.nome}, Moooou")


class Coelho(Animal):
    def __int__(self, nome, cor):
     super().__int__(nome, cor)

    def Pular(self):
        print(f"{self.nome}, Pula e Vive")
