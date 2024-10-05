import flet as ft
from tabla_excel import create_data_table
from notas_grid import create_notas_grid
from galeria_productos import crear_galeria


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800  # Establece el color de fondo
    page.title = "Tabs en Flet"  # Establece el título de la ventana
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crea el título de la aplicación
    titulo = ft.Text("Tabs en Flet", size=24, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)


    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=400,
        tabs=[
            ft.Tab(
                text="Tareas",
                icon=ft.icons.LIST_ALT,
                content=create_data_table(page)
            ),
            ft.Tab(
                text="Notas",
                icon=ft.icons.NOTE,
                content=create_notas_grid(page)
            ),
            ft.Tab(
                text="Galería",
                icon=ft.icons.BROWSE_GALLERY,
                content=crear_galeria(page)
            )
        ],
        expand=1
    )

    page.add(
        titulo,
        tabs
    )

ft.app(main)
