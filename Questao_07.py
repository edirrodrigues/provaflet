'''
Em Python, a orientação a objetos é uma abordagem de programação que permite modelar problemas do mundo real usando objetos e classes.

O que é uma classe em Python?

Uma classe em Python é uma estrutura que define o comportamento e as propriedades de objetos. Uma classe é como um plano ou um molde para criar objetos. Ela define os atributos (variáveis) e métodos (funções) que os objetos daquela classe terão.
Vantagens de utilizar uma classe:

Reutilização de código: As classes permitem encapsular funcionalidades relacionadas, tornando mais fácil reutilizar código em diferentes partes do programa.
Abstração: Classes permitem modelar entidades do mundo real de forma mais abstrata, tornando o código mais legível e manutenível.
Encapsulamento: Classes permitem controlar o acesso aos dados e funcionalidades, melhorando a segurança e a organização do código.
Herança e Polimorfismo: Através da herança, é possível criar novas classes com base em classes existentes, o que promove a reutilização de código. O polimorfismo permite que objetos de diferentes classes sejam tratados de forma uniforme.
Importância da classe em uma programação:

Em uma programação orientada a objetos, as classes são fundamentais. Elas permitem modelar entidades do mundo real de forma estruturada e modular, facilitando a criação, manutenção e expansão do código.
Paradigma de programação:

Um paradigma de programação é uma abordagem ou estilo para resolver problemas de programação. Existem vários paradigmas de programação, como o paradigma imperativo, o paradigma funcional e o paradigma orientado a objetos. Cada paradigma tem suas próprias características e maneiras de abordar os problemas de programação.
O Python é multi paradigma?

Sim, o Python é uma linguagem de programação multi paradigma, o que significa que suporta vários estilos de programação, incluindo programação orientada a objetos, programação imperativa e programação funcional. Isso oferece aos desenvolvedores flexibilidade para escolher a abordagem mais adequada para resolver um determinado problema. Python suporta a orientação a objetos através de sua sintaxe e recursos, como classes e herança, mas também permite o uso de técnicas de programação imperativas e funcionais.

'''

#passo 1 -Criar uma Classe Carro
#passo 2 -Crie Construtores (nome e marca)
#passo 3- Get e Set
#

class Carro:
    def __init__(self,nome,marca): #
       self.nome = nome 
       self.marca = marca
    
    def get_nome(self):
        return self.nome 
    
    def set_nome(self,nome):
        self.nome = nome 

    def get_marca(self):
        return self.marca
    
    def set_marca(self,nova_marca):
        self.marca = nova_marca