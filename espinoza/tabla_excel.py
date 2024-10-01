# Importamos las bibliotecas necesarias
import flet as ft  # Para crear la interfaz gráfica
from openpyxl import Workbook  # Para crear y manipular archivos Excel
from datetime import datetime  # Para generar nombres de archivo únicos


def create_data_table(page: ft.Page):
    # Configuración inicial de la página
    # page.bgcolor = ft.colors.BLUE_GREY_800  # Establece el color de fondo
    # page.title = "DataTable en Flet con Excel"  # Establece el título de la ventana
    # Centra el contenido horizontalmente
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Crea el título de la aplicación
    titulo = ft.Text("DataTable en Flet", size=32, weight=ft.FontWeight.BOLD)

    # Crea los campos de entrada para nombre y edad
    nombre_input = ft.TextField(
        label="Nombre",
        bgcolor=ft.colors.BLUE_GREY_700,
        color=ft.colors.WHITE
    )
    edad_input = ft.TextField(
        label="Edad",
        bgcolor=ft.colors.BLUE_GREY_700,
        color=ft.colors.WHITE
    )

    # Crea la tabla de datos
    tabla = ft.DataTable(
        bgcolor=ft.colors.BLUE_GREY_600,
        border=ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3, ft.colors.BLUE_GREY_200),
        columns=[
            ft.DataColumn(ft.Text("ID", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Nombre", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Edad", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Acciones", color=ft.colors.BLUE_200))
        ],
        rows=[]  # Inicialmente la tabla está vacía
    )

    # Crea un contenedor scrollable para la tabla
    tabla_container = ft.ListView(
        controls=[tabla],
        height=page.height - 100,  # Altura ajustable
        spacing=70,
        padding=50,
        auto_scroll=True  # Permite desplazamiento automático
    )

    def validar_edad(edad):
        """Valida que la edad sea un número entero entre 0 y 120."""
        try:
            edad_int = int(edad)
            return 0 <= edad_int <= 120
        except ValueError:
            return False

    def agregar_fila(e):
        """Agrega una nueva fila a la tabla si los datos son válidos."""
        # Valida que el nombre no esté vacío
        if not nombre_input.value:
            mostrar_mensaje("El nombre no puede estar vacío")
            return
        # Valida que la edad sea correcta
        if not validar_edad(edad_input.value):
            mostrar_mensaje("La edad debe ser un número entre 0 y 120")
            return

        # Crea una nueva fila con los datos ingresados
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(tabla.rows)+1),
                            color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value,
                            color=ft.colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.WHITE)),
                ft.DataCell(ft.Row([
                    ft.IconButton(
                        ft.icons.EDIT,
                        icon_color=ft.colors.YELLOW,
                        on_click=lambda _: editar_fila(nueva_fila)
                    ),
                    ft.IconButton(
                        ft.icons.DELETE,
                        icon_color=ft.colors.RED,
                        on_click=lambda _: eliminar_fila(nueva_fila)
                    )
                ]))
            ]
        )
        tabla.rows.append(nueva_fila)  # Añade la nueva fila a la tabla
        nombre_input.value = ""  # Limpia el campo de nombre
        edad_input.value = ""  # Limpia el campo de edad
        page.update()  # Actualiza la página para mostrar los cambios

    def editar_fila(fila):
        """Carga los datos de una fila en los campos de entrada para su edición."""
        nombre_input.value = fila.cells[1].content.value
        edad_input.value = fila.cells[2].content.value
        eliminar_fila(fila)  # Elimina la fila original
        page.update()

    def eliminar_fila(fila):
        """Elimina una fila de la tabla."""
        tabla.rows.remove(fila)
        actualizar_ids()  # Actualiza los IDs después de eliminar
        page.update()

    def actualizar_ids():
        """Actualiza los IDs de las filas para que sean consecutivos."""
        for i, fila in enumerate(tabla.rows, start=1):
            fila.cells[0].content.value = str(i)

    def guardar_excel(e):
        """Guarda los datos de la tabla en un archivo Excel."""
        wb = Workbook()
        ws = wb.active
        ws.title = "BBDD"
        ws.append(["ID", "Nombre", "Edad"])  # Encabezados
        for row in tabla.rows:
            # Guarda solo las tres primeras columnas (ID, Nombre, Edad)
            ws.append([cell.content.value for cell in row.cells[:3]])

        # Genera un nombre de archivo único con la fecha y hora actual
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"datos_tabla_{fecha_hora}.xlsx"
        wb.save(nombre_archivo)

        mostrar_mensaje(f"Datos guardados en {nombre_archivo}")

    def mostrar_mensaje(mensaje):
        """Muestra un mensaje al usuario usando un SnackBar."""
        snack_bar = ft.SnackBar(content=ft.Text(mensaje))
        page.snack_bar = snack_bar
        page.snack_bar.open = True
        page.update()

    # Crea el botón para agregar filas
    agregar_btn = ft.ElevatedButton(
        "Agregar",
        on_click=agregar_fila,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE
    )

    # Crea el botón para guardar en Excel
    guardar_btn = ft.ElevatedButton(
        "Guardar en Excel",
        on_click=guardar_excel,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.GREEN
    )

    # Crea un contenedor para los campos de entrada y los botones
    input_container = ft.Row(
        controls=[nombre_input, edad_input, agregar_btn, guardar_btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Agrega todos los elementos a la página
    # page.add(titulo, input_container, tabla_container)


# Inicia la aplicación Flet
# ft.app(main)

# Retorna un contenedor con todos los elementos
    return ft.Container(
        content=ft.Column([
            titulo,
            ft.Divider(height=20, color=ft.colors.GREY_100),  # Línea divisoria
            input_container,
            tabla_container
        ], scroll=ft.ScrollMode.AUTO, expand=True),
        expand=True,
        padding=10
    )
