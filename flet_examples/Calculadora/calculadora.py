import flet as ft
from botones import ExtraActionButton, ActionButton, DigitButton

class Calculadora(ft.Container):
    def __init__(self):
        super().__init__()

        # Inicializa el estado de la calculadora
        self.reset()

        # Texto que muestra el resultado
        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        
        # Propiedades del contenedor de la calculadora
        self.width = 350
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20

        # Crea el diseño de la calculadora
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"), # Fila con el resultado
                # Primera fila de botones
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC", button_clicked=self.button_clicked),
                        ExtraActionButton(text="+/-", button_clicked=self.button_clicked),
                        ExtraActionButton(text="%", button_clicked=self.button_clicked),
                        ActionButton(text="/", button_clicked=self.button_clicked)
                    ]
                ),
                # Segunda fila de botones
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="*", button_clicked=self.button_clicked)
                    ]
                ),
                # Tercera fila de botones
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked)
                    ]
                ),
                # Cuarta fila de botones
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked)
                    ]
                ),
                # Quinta fila de botones
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2, button_clicked=self.button_clicked),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked),
                    ]
                )
            ]
        )

    def button_clicked(self, e):
        # Este método se llama cada vez que se presiona un botón
        data = e.control.data # Contiene el texto del botón presionado
        print(f"Botón presionado con dato = {data}")

        # Maneja diferentes clics de botones
        if self.result.value == "Error" or data == "AC":
            # Reinicia la calculadora si hay un error o se presiona AC
            self.result.value = "0"
            self.reset()
        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            # Maneja la entrada de dígitos
            # Si el resultado actual es "0" o new_operand es True, se reemplaza el valor actual con el nuevo dígito
            # Si no, se añade el nuevo dígito al final del número actual
            if self.result.value == "0" or self.new_operand:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data
        elif data in ("+", "-", "*", "/"):
            # Maneja la entrada de operadores
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True
        elif data == "=":
            # Calcula el resultado final
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()
        elif data == "%":
            # Calcula el porcentaje
            self.result.value = float(self.result.value) / 100
            self.reset()
        elif data == "+/-":
            # Cambia el signo del número
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        # Actualiza la interfaz de usuario
        self.update()

    def format_number(self, num):
        # Formatea el número para eliminar ceros a la derecha si es un número entero
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        # Realiza el cálculo basado en el operador
        if operator == "+":
            return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "*":
            return self.format_number(operand1 * operand2)
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        # Reinicia el estado de la calculadora
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True