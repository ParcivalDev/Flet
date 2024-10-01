import flet as ft


class Message():
    def __init__(self, user_name: str, text: str, message_type: str, house: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type
        self.house = house


class ChatMessage(ft.Row):
    # Hereda de ft.Row para crear una fila en la interfaz de Flet
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START

        # Diccionario que asocia cada casa con su color característico
        house_colors = {
            "Gryffindor": ft.colors.RED,
            "Slytherin": ft.colors.GREEN,
            "Ravenclaw": ft.colors.BLUE,
            "Hufflepuff": ft.colors.YELLOW
        }

        # Define los controles que formarán parte de este mensaje en el chat
        # message.house es la clave que estamos buscando en el diccionario
        # ft.colors.GREY es el valor por defecto que se devolverá si la clave no se encuentra en el diccionario
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(message.user_name)),
                color=ft.colors.WHITE,
                bgcolor=house_colors.get(message.house, ft.colors.GREY)
            ),
            # Crea una columna con el nombre de usuario (y su casa) y el texto del mensaje
            ft.Column(
                [
                    ft.Text(
                        f"{message.user_name} ({message.house if message.house else 'Muggle'})", weight="bold"),
                    ft.Text(message.text, selectable=True),
                ],
                spacing=5
            )
        ]

    # Obtiene las iniciales del nombre de usuario
    # Retorna la primera letra del nombre en mayúscula, o "?" si el nombre está vacío
    def get_initials(self, user_name: str):
        return user_name[:1].capitalize() if user_name else "?"
