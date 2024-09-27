import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_700
    page.title = "Vídeo 2: Filas y Columnas"
    texto1 = ft.Text("Texto 1", size=24, color=ft.colors.WHITE)
    texto2 = ft.Text("Texto 2", size=24, color=ft.colors.WHITE)
    texto3 = ft.Text("Texto 3", size=24, color=ft.colors.WHITE)

    fila_textos = ft.Row(
        controls=[texto1, texto2, texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    boton1 = ft.FilledButton("Botón 1")
    boton2 = ft.FilledButton("Botón 2")
    boton3 = ft.FilledButton("Botón 3")

    fila_botones = ft.Row(
        controls=[boton1, boton2, boton3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )
    
    
    textos_columnas = [
        ft.Text("Columna 1 - Fila 1", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 2", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 1 - Fila 3", size=24, color=ft.colors.WHITE)
    ]
    
    
    columnas_textos = ft.Column(
        controls= textos_columnas
    )
    
    textos_columnas2 = [
        ft.Text("Columna 2 - Fila 1", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 2 - Fila 2", size=24, color=ft.colors.WHITE),
        ft.Text("Columna 2 - Fila 3", size=24, color=ft.colors.WHITE)
    ]
    
    
    columnas_textos2 = ft.Column(
        controls= textos_columnas2
    )
    
    fila_columnas = ft.Row(
        controls=[columnas_textos, columnas_textos2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing= 50
        
    )
    page.add(fila_textos, fila_botones, fila_columnas)
    

ft.app(main)
