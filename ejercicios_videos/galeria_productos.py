# Importamos las bibliotecas necesarias
import flet as ft  # Flet para crear la interfaz gráfica
import os  # Para manejar rutas de archivos
import base64  # Para codificar imágenes en base64

# Función principal que configura y ejecuta la aplicación


def crear_galeria(page: ft.Page):
    # Configuración básica de la página
    # page.title = "Galería de Productos Responsiva"
    # page.theme_mode = ft.ThemeMode.DARK  # Modo oscuro
    # page.bgcolor = ft.colors.BLUE_GREY_900  # Color de fondo

    # Título de la galería
    titulo = ft.Text("Galería de Productos", size=32,
                     weight=ft.FontWeight.BOLD)

    # Función para crear un producto individual
    def crear_producto(nombre, precio, color, img_nombre):
        # Construimos la ruta de la imagen
        imagen_path = os.path.join(
            os.path.dirname(__file__), "assets", img_nombre)

        # Intentamos abrir y codificar la imagen
        try:
            with open(imagen_path, "rb") as image_file:
                image_bytes = base64.b64encode(image_file.read()).decode()
        except FileNotFoundError:
            print(f"Error: La imagen {img_nombre} no existe en {imagen_path}")
            image_bytes = None

        # Creamos y retornamos un contenedor con la información del producto
        return ft.Container(
            content=ft.Column([
                # Mostramos la imagen si se pudo cargar, si no, un mensaje de error
                ft.Image(
                    src_base64=image_bytes,
                    width=150,
                    height=150,
                    fit=ft.ImageFit.CONTAIN,  # Ajusta la imagen manteniendo su proporción
                    error_content=ft.Text("Imagen no encontrada")
                ) if image_bytes else ft.Text("Imagen no encontrada"),
                ft.Text(nombre, size=16, weight=ft.FontWeight.BOLD),
                ft.Text(f"{precio} €", size=14),
                ft.ElevatedButton("Agregar al carrito", color=ft.colors.WHITE)
            ]),
            bgcolor=color,  # Color de fondo del contenedor
            border_radius=10,  # Bordes redondeados
            padding=20,  # Espacio interno
            alignment=ft.alignment.center  # Alineación del contenido
        )

    # Lista de productos
    productos = [
        crear_producto("Producto 1", 19.99,
                       ft.colors.BLUE_500, "producto1.png"),
        crear_producto("Producto 2", 29.99,
                       ft.colors.GREEN_500, "producto2.png"),
        crear_producto("Producto 3", 39.99,
                       ft.colors.ORANGE_500, "producto3.png"),
        crear_producto("Producto 4", 49.99,
                       ft.colors.PURPLE_500, "producto4.png"),
        crear_producto("Producto 5", 59.99,
                       ft.colors.AMBER_500, "producto5.png"),
        crear_producto("Producto 6", 69.99,
                       ft.colors.BLUE_GREY_500, "producto6.png"),
        crear_producto("Producto 7", 79.99,
                       ft.colors.BROWN_500, "producto7.png"),
        crear_producto("Producto 8", 89.99,
                       ft.colors.DEEP_ORANGE_500, "producto8.png")
    ]

    # Creamos una galería responsiva con los productos
    galeria = ft.ResponsiveRow(
        # Creamos un contenedor para cada producto con configuración responsiva
        [ft.Container(producto, col={"sm": 12, "md": 6, "lg": 3})
         for producto in productos],
        run_spacing=20,  # Espacio vertical entre filas
        spacing=20  # Espacio horizontal entre columnas
    )

    # Envolvemos la galería en un ScrollableColumn para permitir desplazamiento
    contenido_scrollable = ft.Column(
        controls=[
            titulo,
            ft.Divider(height=20, color=ft.colors.GREY_100),  # Línea divisoria
            galeria
        ],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,  # Habilita el scroll automático
        expand=True  # Permite que el contenido ocupe todo el espacio disponible
    )

    # Añadimos el contenido scrollable a la página
#     page.add(contenido_scrollable)

# # Iniciamos la aplicación
# ft.app(main)

    return contenido_scrollable
