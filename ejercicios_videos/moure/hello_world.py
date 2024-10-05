import flet as ft
import time
def main(page: ft.Page):
    t = ft.Text()    
    page.add(t)
    
    for i in range(10):
        t.value = f"Hola {i}"
        page.update()
        time.sleep(1)
        
    if t.value == "Hola 9":
        t.value = "Fin"
        
        for i in range(100):
            page.controls.append(ft.TextButton(f"Hola {i}"))
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS
    page.update()
        
    
ft.app(main)
# ft.app(main, view=ft.AppView.WEB_BROWSER)

