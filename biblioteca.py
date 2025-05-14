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
        print(f" O valor do seu ingresso R$ {self.valor}")



class Vip(Ingresso):
    def __init__(self, valor):
      super().__init__(valor * 1.5)
    def imprimirValor(self):
        print(f" O Igresso Vip R$ {self.valor}")




class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularPerimetro(self,base,altura):
        self.perimetro=(base+altura)*2
        print(f"Calculo da Area do Retangulo é: {self.perimetro}")

    def calcularArea(self,base,altura):
       self.area =base*altura
       print(f"Calculo do Perimetro do Retangulo é: {self.area}")

class Triangulo(Forma):
    def __init__(self,base, altura):
        super().__init__()
        self.base=base
        self.altura=altura

    def calculaArea(self):
        self.area=(self.base*self.altura)/2
        print(self.area)
    def calculaPerimetro(self):
        self.perimetro= self.base*3
        print(self.perimetro)
