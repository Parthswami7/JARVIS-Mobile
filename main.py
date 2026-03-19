import flet as ft
import traceback
import tempfile
import os
import time

def main(page: ft.Page):
    try:
        page.title = "JARVIS"
        page.theme_mode = ft.ThemeMode.DARK
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # We import here so if Android blocks it, it prints the error on screen!
        from gtts import gTTS

        # --- SETUP AUDIO ---
        audio_player = ft.Audio(autoplay=True)
        mic_recorder = ft.AudioRecorder()
        page.overlay.extend([audio_player, mic_recorder])

        status_text = ft.Text("JARVIS IS ONLINE", size=20, color="cyan")
        chat_history = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

        def speak(text):
            tts = gTTS(text=text, lang='en')
            # FIX: Android requires us to save audio to a temporary cache folder
            temp_dir = tempfile.gettempdir()
            filepath = os.path.join(temp_dir, "jarvis_response.mp3")
            tts.save(filepath)
            
            audio_player.src = filepath
            audio_player.update()

        def process_audio():
            time.sleep(1)
            chat_history.controls.append(ft.Text("Parth_Sir: [Audio Command Sent]", color="white"))
            response = "Hello Parth Sir. My mobile audio systems are fully operational."
            chat_history.controls.append(ft.Text(f"JARVIS: {response}", color="cyan"))
            speak(response)
            status_text.value = "JARVIS IS ONLINE"
            page.update()

        def handle_mic_tap(e):
            if mic_recorder.status == ft.AudioRecorderStatus.RECORDING:
                mic_recorder.stop_recording()
                status_text.value = "Processing..."
                page.update()
                process_audio()
            else:
                # FIX: Save mic recordings to the temp folder as well
                temp_dir = tempfile.gettempdir()
                mic_filepath = os.path.join(temp_dir, "user_command.wav")
                mic_recorder.start_recording(mic_filepath)
                status_text.value = "Listening... (Tap to stop)"
                page.update()

        # --- UI LAYOUT ---
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Image(src="https://i.imgur.com/8QG9Xn8.png", width=150),
                    status_text,
                    ft.Divider(),
                    chat_history,
                    ft.FloatingActionButton(icon=ft.Icons.MIC, on_click=handle_mic_tap, bgcolor="cyan")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20,
                expand=True
            )
        )

    except Exception as e:
        # IF IT CRASHES, DRAW THE RAW ERROR TO THE PHONE SCREEN
        error_msg = traceback.format_exc()
        page.add(
            ft.Text("SYSTEM BOOT FAILURE", color="red", size=25, weight="bold"),
            ft.Text("Show this error to the terminal:", color="yellow"),
            ft.Container(
                content=ft.Text(error_msg, color="white", size=10, selectable=True),
                bgcolor="black",
                padding=10,
                border_radius=10
            )
        )
        page.update()

ft.app(target=main)
