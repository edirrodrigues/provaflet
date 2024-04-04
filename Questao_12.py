import flet as ft   



def main(page:ft.Page):
    cab= ft.Text("Lista de exercícios")

    btn01 =ft.ElevatedButton("Questão 01", on_click=quest01)
        
    page.add(cab,btn01)


ft.app(target=main)





