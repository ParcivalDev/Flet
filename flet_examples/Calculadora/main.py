import flet as ft
from calculadora import Calculadora


def main(page: ft.Page):
    page.title = "Calculadora"

    calculadora = Calculadora()
    page.add(calculadora)


ft.app(main)
