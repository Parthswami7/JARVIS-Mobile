import flet as ft
from gtts import gTTS
import time
import os

def main(page: ft.Page):
    page.title = "JARVIS Mobile"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- 1. SETUP MOBILE AUDIO HARDWARE ---
    audio_player = ft.Audio(autoplay=True)
    mic_recorder = ft.AudioRecorder()
    page.overlay.extend([audio_player, mic_recorder])

    status_text = ft.Text("JARVIS IS ONLINE", size=20, color="cyan")
    chat_history = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    # --- 2. THE MOBILE MOUTH (TTS) ---
    def speak(text):
        # Generate the audio file using Google TTS
        tts = gTTS(text=text, lang='en')
        filepath = "jarvis_response.mp3"
        tts.save(filepath)
        
        # Tell Android to play the file
        audio_player.src = filepath
        audio_player.update()

    # --- 3. THE BRAIN LOGIC ---
    def process_audio():
        # This is where your AI Brain (like Gemini) will go!
        # For now, it's a simulation to test the Android audio system
        time.sleep(1) 
        
        chat_history.controls.append(ft.Text("Parth_Sir: [Audio Command Sent]", color="white"))
        
        response = "Hello Parth Sir. My mobile audio systems are now fully operational."
        chat_history.controls.append(ft.Text(f"JARVIS: {response}", color="cyan"))
        
        speak(response)
        
        status_text.value = "JARVIS IS ONLINE"
        page.update()

    # --- 4. THE MOBILE EARS (STT) ---
    def handle_mic_tap(e):
        # If already recording, stop it and process
        if mic_recorder.status == ft.AudioRecorderStatus.RECORDING:
            mic_recorder.stop_recording()
            status_text.value = "Processing Audio..."
            page.update()
            process_audio()
        # If not recording, start listening
        else:
            # Saves your voice to a file on the phone
            mic_recorder.start_recording("user_command.wav")
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

ft.app(target=main)
