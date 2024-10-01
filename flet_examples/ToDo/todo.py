import flet as ft
from task import Task

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        
        # Campo de texto para ingresar nuevas tareas
        self.nueva_tarea = ft.TextField(
            hint_text="Escribe una tarea...", 
            expand=True,  # Permite que el campo de texto se expanda para llenar el espacio disponible
            border_color=ft.colors.BLUE_400,  # Color del borde cuando el campo no está enfocado
            focused_border_color=ft.colors.BLUE_600  # Color del borde cuando el campo está enfocado
        )
        
        # Columna para almacenar las tareas
        self.tareas = ft.Column()
        
        # Pestañas para filtrar las tareas
        self.filtrar = ft.Tabs(
            selected_index=0,  # Índice de la pestaña seleccionada por defecto
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="Todas"), ft.Tab(text="Activas"), ft.Tab(text="Completadas")],
        )
        
        # Texto para mostrar el número de tareas restantes
        self.tareas_restantes = ft.Text("Tareas restantes: 0")
        
        # Contenedor principal con toda la interfaz de usuario
        main_container = ft.Container(
            width=600,  # Ancho fijo del contenedor
            padding=20,  # Espacio alrededor del contenido del contenedor
            bgcolor=ft.colors.WHITE, 
            border_radius=10, 
            content=ft.Column(
                controls=[
                    # Título de la aplicación
                    ft.Text(value="Tareas", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.BLUE_600),
                    # Fila con campo de texto y botón para agregar tarea
                    ft.Row(
                        controls=[
                            self.nueva_tarea,
                            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.agrega_tarea)
                        ]
                    ),
                    # Columna con filtros, lista de tareas y controles adicionales
                    ft.Column(
                        spacing=25,  # Espacio vertical entre los controles de esta columna
                        controls=[
                            self.filtrar,
                            self.tareas,
                            # Fila con contador de tareas y botón para borrar completadas
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Alinea los elementos a los extremos
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                                controls=[
                                    self.tareas_restantes,
                                    ft.ElevatedButton(
                                        text="Borrar completadas",
                                        on_click=self.borrar_completas,
                                        style=ft.ButtonStyle(
                                            color=ft.colors.RED_400,  
                                            bgcolor=ft.colors.RED_50,  
                                        )
                                    ),
                                ],
                            )
                        ]
                    )
                ]
            )
        )
        
        # Añadimos el contenedor principal a los controles de esta columna
        self.controls = [main_container]
    
    def borrar_completas(self, e):
        # Recorremos una copia de la lista para evitar problemas al modificar durante la iteración
        for tarea in self.tareas.controls[:]:
            if tarea.completed:
                self.borra_tarea(tarea)
    
    def agrega_tarea(self, e):
        if self.nueva_tarea.value:
            # Creamos una nueva tarea y la añadimos a la lista
            # Pasamos tres argumentos: el texto de la tarea, y dos métodos
            tarea = Task(self.nueva_tarea.value, self.cambia_estado_tarea, self.borra_tarea)
            self.tareas.controls.append(tarea)
            self.nueva_tarea.value = ""  # Limpiamos el campo de texto
            self.update()  
    
    def borra_tarea(self, tarea):
        # Eliminamos la tarea de la lista y actualizamos la interfaz
        self.tareas.controls.remove(tarea)
        self.update()
    
    def update(self):
        # Obtenemos el estado actual del filtro
        status = self.filtrar.tabs[self.filtrar.selected_index].text.lower()
        count = 0
        for task in self.tareas.controls:
            # Actualizamos la visibilidad de cada tarea según el filtro seleccionado
            task.visible = (
                status == "todas"
                or (status == "activas" and not task.completed)
                or (status == "completadas" and task.completed)
            )
            if not task.completed:
                count += 1
        # Actualizamos el contador de tareas restantes
        self.tareas_restantes.value = f"Tareas restantes: {count}"
        super().update()
    
    def cambia_estado_tarea(self):
        # Este método se llama cuando cambia el estado de una tarea (completada o no)
        self.update()
    
    def tabs_changed(self, e):
        # Este método se llama cuando se cambia la pestaña de filtrado
        self.update()