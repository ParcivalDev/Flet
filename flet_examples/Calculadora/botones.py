import flet as ft

# Clase base para todos los botones de la calculadora
class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()  
        self.text = text  # Texto que se mostrará en el botón
        self.on_click = button_clicked  # Función que se ejecutará al hacer clic
        self.data = text  # Datos asociados al botón (en este caso, el mismo texto)
        self.expand = expand  # Factor de expansión del botón en su contenedor

# Clase para los botones de dígitos (0-9 y punto decimal)
class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)  # Inicializa la clase padre
        self.bgcolor = ft.colors.WHITE24 
        self.color = ft.colors.WHITE  

# Clase para los botones de acción (operadores: +, -, *, /, =)
class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE 

# Clase para los botones de acción extra (AC, +/-, %)
class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked) 
        self.bgcolor = ft.colors.BLUE_GREY_100  
        self.color = ft.colors.BLACK 