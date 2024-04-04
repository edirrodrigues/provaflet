# Ler o número inteiro de 1 a 7
numero = int(input("Digite um número de 1 a 7: "))

# Verificar o dia da semana correspondente
if numero == 1:
    dia_semana = "Domingo"
elif numero == 2:
    dia_semana = "Segunda-feira"
elif numero == 3:
    dia_semana = "Terça-feira"
elif numero == 4:
    dia_semana = "Quarta-feira"
elif numero == 5:
    dia_semana = "Quinta-feira"
elif numero == 6:
    dia_semana = "Sexta-feira"
elif numero == 7:
    dia_semana = "Sábado"
else:
    dia_semana = "Número inválido"

# Mostrar o dia da semana correspondente
print("O número", numero, "corresponde a", dia_semana)