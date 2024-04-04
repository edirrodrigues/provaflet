
"""

    Passo 1- Ler um número inteiro
    Passo 2 -Verificar se o número é de 1 até 12
    Passo 3 - Mostre o dia respectivo da semana.

"""

def main():
    numero = int(input("Digite um número de 1 a 12: ")) #passo 1
    nome_mes = obter_nome_mes(numero) 
    print(f"O mês correspondente ao número {numero} é: {nome_mes}")#passo 3



def obter_nome_mes(numero):
    match numero:  #passo 2
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3: 
            return "Março"
        case 4: 
            return "Abril"
        case 5: 
            return "Maio"
        case 6:
            return "junho"
        case 7:
            return "julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11: 
            return "Novembro"
        case 12:
            return "Dezembro"
        case _:
            return "Número Inválido" 



if __name__ == "__main__":
    main()

                                                               