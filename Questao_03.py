# Ler os valores das variáveis
nome_maquina = input("Digite o nome da máquina: ")
tempo_uso = int(input("Digite o tempo de uso da máquina (em anos): "))
ligado = input("A máquina está ligada? (sim/não): ").lower() == "sim"

# Mostrar os valores lidos e seus tipos
print("\nValores lidos:")
print("Nome da máquina:", nome_maquina, "- Tipo:", type(nome_maquina))
print("Tempo de uso:", tempo_uso, "- Tipo:", type(tempo_uso))
print("Ligado:", ligado, "- Tipo:", type(ligado))