class Carro:
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca


# Criando uma instância da classe Carro
meu_carro = Carro("Civic", "Honda")

# Usando os métodos get para acessar os atributos
print("Nome do carro:", meu_carro.get_nome())
print("Marca do carro:", meu_carro.get_marca())

# Usando os métodos set para modificar os atributos
meu_carro.set_nome("Corolla")
meu_carro.set_marca("Toyota")

# Usando os métodos get novamente para verificar as modificações
print("Nome do carro atualizado:", meu_carro.get_nome())
print("Marca do carro atualizada:", meu_carro.get_marca())