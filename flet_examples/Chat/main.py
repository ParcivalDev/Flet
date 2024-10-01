import flet as ft
from flet import ControlEvent, Container
from message import Message, ChatMessage


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.padding = 0
    page.window.width = 600
    page.window.height = 700
    page.title = "Hogwarts Chat"

    # Función que se ejecuta cuando se recibe un nuevo mensaje
    def on_message(message: Message):
        if message.message_type == "chat_message":
            # Mensaje normal de chat
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            # Mensaje de login, mostrado en itálica
            m = ft.Text(
                message.text,
                italic=True,
                color=ft.colors.BLUE_200,
                size=14
            )
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # Función que se ejecuta cuando se envía un mensaje
    def send_click(e):
        if new_message.value:  # Si hay texto en el campo de mensaje
            # Envía el mensaje a todos los usuarios
            page.pubsub.send_all(
                Message(user_name=page.session.get("user_name"),
                        text=new_message.value,
                        message_type="chat_message",
                        house=page.session.get("house")))
            new_message.value = ""
            emoji_picker.visible = False
            new_message.focus()
            page.update()

    # Función que se ejecuta cuando un usuario se une al chat
    def join_click(e):
        # Si no se ingresó un nombre o no se seleccionó una casa, muestra un error
        if not join_user_name.value or house_dropdown.value == "Selecciona tu casa":
            join_user_name.error_text = "Ingresa tu nombre y selecciona tu casa!"
            join_user_name.update()
        else:
            # Guarda el nombre de usuario y la casa en la sesión
            page.session.set("user_name", join_user_name.value)
            page.session.set("house", house_dropdown.value)
            dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            # Envía un mensaje de login a todos los usuarios
            page.pubsub.send_all(Message(
                user_name=join_user_name.value,
                text=f"{join_user_name.value} se ha unido al chat desde la casa {house_dropdown.value}.",
                message_type="login_message",
                house=house_dropdown.value))
            page.update()

    # Campo de texto para ingresar el nombre de usuario
    join_user_name = ft.TextField(
        label="Ingresa tu nombre de mago",
        autofocus=True
    )

    # Menú desplegable para seleccionar la casa de Hogwarts
    house_dropdown = ft.Dropdown(
        label="Selecciona tu casa",
        options=[
            ft.dropdown.Option(
                text="Gryffindor",
                content=ft.Row(
                    [ft.Icon(ft.icons.LOCAL_FIRE_DEPARTMENT), ft.Text("Gryffindor")]),
            ),
            ft.dropdown.Option(
                text="Slytherin",
                content=ft.Row(
                    [ft.Icon(ft.icons.STORM), ft.Text("Slytherin")]),
            ),
            ft.dropdown.Option(
                text="Ravenclaw",
                content=ft.Row(
                    [ft.Icon(ft.icons.AUTO_STORIES), ft.Text("Ravenclaw")]),
            ),
            ft.dropdown.Option(
                text="Hufflepuff",
                content=ft.Row(
                    [ft.Icon(ft.icons.GRASS), ft.Text("Hufflepuff")]),
            ),
        ],
        width=200
    )

    # Diálogo de bienvenida que se muestra al iniciar la aplicación
    dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Bienvenido a Hogwarts!"),
        content=ft.Column([join_user_name, house_dropdown],
                          width=300, height=150, tight=True),
        actions=[ft.ElevatedButton(
            text="Unirse al chat", on_click=join_click)],
        actions_alignment=ft.MainAxisAlignment.END
    )
    # Añade el diálogo a la superposición de la página
    page.overlay.append(dialog)

    # Lista de vista para mostrar los mensajes del chat
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        padding=20
    )

    # Campo de texto para escribir nuevos mensajes
    new_message = ft.TextField(
        hint_text="Escribe un hechizo... digo, un mensaje...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_click,
        border_color=ft.colors.BLUE_200,
        bgcolor=ft.colors.BLUE_GREY_800
    )

    emoji_list = [
        "🧙", "🔮", "⚡", "🦉", "🧹", "🧪", "📜", "🏰", "🐍", "🦁",
        "🦅", "🦡", "🚂", "🕯️", "🧬", "🗝️", "⏳", "🧣", "👓", "⚗️"
    ]

    # Selector de emojis
    emoji_picker = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=50,
        spacing=5,
        run_spacing=5,
        visible=False  # Inicialmente oculto
    )

    # Añade cada emoji al selector
    for emoji_char in emoji_list:
        emoji_picker.controls.append(
            ft.Container(
                content=ft.Text(emoji_char, size=24),
                on_click=lambda e: emoji_selected(e),
                data=emoji_char
            )
        )

    # Función que se ejecuta cuando se selecciona un emoji
    def emoji_selected(e: ControlEvent):
        item = e.control
        if isinstance(item, Container):
            new_message.value += item.data
            new_message.focus()
            new_message.update()

    # Función para mostrar/ocultar el selector de emojis
    def toggle_emoji_picker(e):
        emoji_picker.visible = not emoji_picker.visible
        page.update()

    # Barra superior de la aplicación
    app_bar = ft.AppBar(
        leading=ft.Icon(ft.icons.CASTLE),
        leading_width=40,
        title=ft.Text("Chat de Hogwarts"),
        center_title=False,
        bgcolor=ft.colors.BLUE_GREY_700,
        actions=[
            ft.IconButton(ft.icons.AUTO_FIX_HIGH),
            ft.IconButton(ft.icons.BOOK),
            ft.IconButton(ft.icons.MORE_VERT)
        ]
    )

    # Contenedor principal del chat
    chat_container = ft.Container(
        content=chat,
        expand=True
    )

    # Barra inferior para escribir mensajes
    message_bar = ft.Container(
        content=ft.Column([
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.EMOJI_EMOTIONS_OUTLINED,
                        icon_color=ft.colors.BLUE_200,
                        on_click=toggle_emoji_picker,
                    ),
                    new_message,
                    ft.IconButton(
                        icon=ft.icons.SEND_ROUNDED,
                        icon_color=ft.colors.BLUE_200,
                        on_click=send_click,
                    ),
                ],
                spacing=0,
            ),
            emoji_picker,
        ]),
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_800,
        border=ft.border.only(top=ft.border.BorderSide(1, ft.colors.BLUE_200))
    )

    page.add(
        app_bar,
        chat_container,
        message_bar,
    )


ft.app(target=main)
