# alphabet_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
import os

class AlphabetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_alphabet_grid()

    def create_alphabet_grid(self):
        layout = GridLayout(cols=4, padding=10, spacing=10)
        letters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        
        for letter in letters:
            btn = Button(text=letter, font_size=24)
            btn.bind(on_release=self.show_letter)
            layout.add_widget(btn)
        
        # Agregar el botón "Volver al Menú"
        btn_back = Button(text='Volver al Menú', size_hint_y=None, height=50)
        btn_back.bind(on_release=self.go_to_menu)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)

    def show_letter(self, instance):
        letter = instance.text
        image_path = os.path.join('assets', 'images', f'{letter}.png')
        sound_path = os.path.join('assets', 'sounds', f'{letter}.mp3')
        
        content = BoxLayout(orientation='vertical', spacing=10)
        
        if os.path.isfile(image_path):
            img = Image(source=image_path, size_hint=(None, None), size=(200, 200))
            content.add_widget(img)
        else:
            content.add_widget(Label(text=f'No image for {letter}', font_size=24))
        
        content.add_widget(Label(text=f'{letter}', font_size=24))

        sound = SoundLoader.load(sound_path)
        if sound:
            sound.play()
        else:
            print(f'Sound file not found for {letter}')
        
        popup = Popup(title=f'Letra: {letter}', content=content, size_hint=(None, None), size=(300, 300))
        popup.open()

    def go_to_menu(self, instance):
        self.manager.current = 'menu'
