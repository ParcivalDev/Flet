import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.title = "Vídeo 1: Texto y Botón que cambia texto"
    texto = ft.Text("Mi primera app")
    texto2 = ft.Text("Esto es un texto que va cambiar")
    
    def cambia_texto(e):
        texto2.value = "Nuevo texto"
        page.update()

    boton = ft.FilledButton(text= "Cambiar texto", on_click=cambia_texto)
    
    page.add(texto, texto2, boton)
        
   
    
ft.app(main)