import flet as ft
import time

def main(page: ft.Page):
    page.title = "JARVIS Mobile"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # JARVIS Status Text
    status_text = ft.Text("JARVIS IS ONLINE", size=20, color="cyan")
    chat_history = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def on_speak_click(e):
        # This is where your AI Brain logic goes!
        status_text.value = "Listening..."
        page.update()
        time.sleep(2) # Simulating processing
        status_text.value = "JARVIS IS ONLINE"
        chat_history.controls.append(ft.Text("User: Hello JARVIS", color="white"))
        chat_history.controls.append(ft.Text("JARVIS: Hello Parth Sir, how can I help?", color="cyan"))
        page.update()

    # The UI Layout
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Image(src="https://i.imgur.com/8QG9Xn8.png", width=150), # Replace with your Arc Reactor icon
                status_text,
                ft.Divider(),
                chat_history,
                ft.FloatingActionButton(icon=ft.Icons.MIC, on_click=on_speak_click, bgcolor="cyan")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            expand=True
        )
    )

ft.app(target=main)