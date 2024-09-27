import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100, read_only=True)
    

# Aquí usamos max(0, ...) porque:
# Estamos restando 1 al valor actual.
# Queremos que el resultado no sea menor que 0.
# max nos da el valor más grande entre 0 y el resultado de la resta.
# Por ejemplo: Si el valor actual es 3, 3 - 1 = 2, y max(0, 2) es 2.

    def minus_click(e):
        txt_number.value = str(max(0, int(txt_number.value) - 2))
        page.update()

    def plus_click(e):
        txt_number.value = str(min(20, int(txt_number.value) + 1))
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)