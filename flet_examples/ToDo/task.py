import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__() 
        self.completed = False  # Estado inicial de la tarea
        self.task_name = task_name 
        self.task_status_change = task_status_change 
        self.task_delete = task_delete  

        # Crea un checkbox para la tarea
        self.display_task = ft.Checkbox(
            value=False,
            label=self.task_name,
            on_change=self.status_changed
        )
        
        # Campo de texto para editar el nombre de la tarea
        self.edit_name = ft.TextField(expand=1)

        # Vista principal de la tarea (checkbox y botones de editar/eliminar)
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Editar tarea",
                            on_click=self.edit_clicked
                        ),
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Eliminar tarea",
                            on_click=self.delete_clicked
                        )
                    ]
                )
            ]
        )

        # Vista de edición de la tarea (inicialmente oculta)
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Actualizar tarea",
                    on_click=self.save_clicked,
                ),
            ],
        )

        # Agrega las vistas a los controles de la columna
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        # Cambia a la vista de edición
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        # Guarda los cambios y vuelve a la vista normal
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        # Actualiza el estado de completado y notifica al padre
        self.completed = self.display_task.value
        self.task_status_change()

    def delete_clicked(self, e):
        # Notifica al padre para eliminar esta tarea
        self.task_delete(self)