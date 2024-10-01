import flet as ft
from todo import TodoApp

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "ToDo App"
    
    # Centramos el contenido horizontalmente en la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Establecemos el color de fondo de la página
    page.bgcolor = ft.colors.BLUE_GREY_50
    
    todo = TodoApp()
    
    page.add(todo)

ft.app(target=main)