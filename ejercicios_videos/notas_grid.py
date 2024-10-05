import flet as ft  # Importamos la biblioteca flet y la nombramos como ft para abreviar


def create_notas_grid(page: ft.Page):
    # Configuración inicial de la página
    # page.title = "Tablero de Notas Adhesivas"  # Establece el título de la ventana
    # page.bgcolor = ft.colors.GREY_800  # Establece el color de fondo de la página
    # page.window.width = 600  # Establece el ancho de la ventana
    # page.window.height = 500  # Establece el alto de la ventana
    # page.theme_mode = "light"  # Establece el tema de la aplicación a modo claro
    # page.padding = 20  # Añade un padding de 20 píxeles alrededor del contenido de la página
    # page.window.center()  # Centra la ventana en la pantalla

    # Función para borrar una nota específica
    def borrar_nota(nota):
        grid.controls.remove(nota)  # Elimina la nota del grid
        page.update()  # Actualiza la página para reflejar los cambios

    # Función para agregar una nueva nota
    def agregar_nota(e):
        # Crea una nueva nota con texto predeterminado
        nueva_nota = crear_nota("Nueva nota")
        grid.controls.append(nueva_nota)  # Añade la nueva nota al grid
        page.update()  # Actualiza la página para mostrar la nueva nota

    # Función para crear una nota individual
    def crear_nota(texto):
        # Crea el campo de texto de la nota
        nota_content = ft.TextField(
            value=texto,  # Texto inicial de la nota
            multiline=True,  # Permite múltiples líneas de texto
            bgcolor=ft.colors.GREY_500,  # Color de fondo del campo de texto
            text_style=ft.TextStyle(color=ft.colors.BLACK)
        )

        # Crea el contenedor de la nota con el texto y un botón de borrar
        nota = ft.Container(
            content=ft.Column([  # Columna que contiene el texto y el botón de borrar
                nota_content,
                ft.IconButton(
                    icon=ft.icons.DELETE,  # Icono de borrar
                    # Función lambda para borrar la nota
                    on_click=lambda _: borrar_nota(nota),
                    icon_color=ft.colors.RED
                )
            ]),
            width=200,  # Ancho del contenedor de la nota
            height=200,  # Alto del contenedor de la nota
            bgcolor=ft.colors.GREY_300,  # Color de fondo de la nota
            border_radius=15,  # Bordes redondeados
            padding=10  # Espacio interno de la nota
        )
        return nota  # Devuelve la nota creada

    # Crea el grid para contener las notas
    grid = ft.GridView(
        expand=True,  # Permite que el grid se expanda para llenar el espacio disponible
        max_extent=220,  # Tamaño máximo de cada celda del grid
        # Relación de aspecto de las celdas (cuadradas en este caso)
        child_aspect_ratio=1
    )

    # Crea algunas notas iniciales
    notas = [
        crear_nota("Primera nota"),
        crear_nota("Segunda nota"),
        crear_nota("Tercera nota"),
    ]
    # Añade las notas iniciales al grid
    for nota in notas:
        grid.controls.append(nota)

    # Crea el título de la aplicación
    texto = ft.Text(
        "Mis Notas Adhesivas",
        weight=ft.FontWeight.BOLD,  # Texto en negrita
        size=18,  # Tamaño de fuente
        color=ft.colors.WHITE  # Color del texto
    )

    # Crea el botón para añadir nuevas notas
    icono = ft.IconButton(
        icon=ft.icons.ADD,  # Icono de añadir
        on_click=agregar_nota,  # Función que se ejecuta al hacer clic
        icon_color=ft.colors.BLUE  # Color del icono
    )

    # Añade los elementos a la página
    # page.add(
    #     ft.Row(  # Fila que contiene el título y el botón de añadir
    #         controls=[texto, icono],
    #         # Alinea los elementos a los extremos
    #         alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    #     ),
    #     grid  # Añade el grid de notas a la página
    # )

    # page.update()  # Actualiza la página para mostrar todos los elementos añadidos


# Inicia la aplicación Flet
# ft.app(main)

    return ft.Container(
        content=ft.Column([
            ft.Row(
                controls=[texto, icono],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            grid
        ]),
        expand=True,
        bgcolor=ft.colors.GREY_800,  # Fondo oscuro solo para el contenedor de notas
        padding=20
    )
