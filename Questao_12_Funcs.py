import flet as ft 

# def quest01(page:ft.Page):
#     1
#     mensagem = ft.Text("Alô, Mundo!")
#     page.add(mensagem)
# ft.app(quest01)
# #*************************************************************************************
# def quest02(page:ft.Page):
#     2
#     mensagem = ft.Text("Digite um nome em letras minúsculas:")
#     nome = ft.TextField(label="Digite o nome:")

#     def btn_click(e):

#          nome_maiusculo = ft.Text(nome.value.upper())
#          nome.value = ""
#          page.add(nome_maiusculo)
#          page.update()

#     btn = ft.ElevatedButton("Transformar em maiúsculo", on_click=btn_click)
#     page.update()
#     page.add(mensagem, nome,btn)

# ft.app(quest02)
#*************************************************************************************

def quest03(page:ft.Page):
    mensagem01 = ft.Text("Nome da máquina:")
    nome_maquina = ft.TextField(label="Nome:")

    mensagem02 = ft.Text("Tempo de uso:")
    tempo_uso = ft.TextField(label="Tempo:")

    mensagem03 = ft.Text("Ligado")

    ligado = ft.Text(type(True))

   


    def btn_click(e):

        mensagem001 = ft.Text(f"Nome: {nome_maquina} - Tipo: {type(nome_maquina)}")
        mensagem002 = ft.Text(f"Tempo de uso: {tempo_uso} - Tipo: {type(tempo_uso)}")
        mensagem003 = ft.Text(f"Estado: {mensagem03} - Tipo: {type(ligado)}")
        page.add(mensagem001, mensagem002, mensagem003)

    btn = ft.ElevatedButton("Verificar", on_click=btn_click)

    page.add(mensagem01,nome_maquina,mensagem02,tempo_uso,mensagem03, btn)