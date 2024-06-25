from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
import random

class ColorMatchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letters_colors = [
            ('A', 'arbol', 'verde'),
            ('B', 'balon', 'azul'),
            ('C', 'casa', 'rojo'),
            ('D', 'dinosaurio', 'amarillo')
        ]
        self.current_letter = None
        self.game_started = False  # Flag para controlar si el juego ha comenzado
        self.create_color_match_game()

    def create_color_match_game(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Etiqueta para mostrar la letra
        self.letter_label = Label(text='', font_size=48, size_hint_y=0.2)
        layout.add_widget(self.letter_label)
        
        # Imagen para mostrar el objeto correspondiente
        self.image = Image(source='', size_hint_y=0.4)
        layout.add_widget(self.image)

        # Contenedor para los botones de colores
        self.color_buttons = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        
        # Crear botones de colores
        colors = ['rojo', 'verde', 'azul', 'amarillo']
        for color in colors:
            color_btn = Button(text=color.capitalize(), font_size=24, background_color=self.get_color_value(color))
            color_btn.bind(on_release=lambda inst, c=color: self.check_color_match(c))
            self.color_buttons.add_widget(color_btn)
            
        # Agregar el botón "Volver al Menú"
        btn_back = Button(text='Volver al Menú', size_hint_y=None, height=50)
        btn_back.bind(on_release=self.go_to_menu)
        layout.add_widget(btn_back)
        
        layout.add_widget(self.color_buttons)
        
        # Botón para iniciar la siguiente ronda
        self.next_button = Button(text='Siguiente', font_size=24, size_hint_y=0.1)
        self.next_button.bind(on_release=self.next_round)
        layout.add_widget(self.next_button)

        # Limpiar widgets previos y añadir el nuevo layout
        self.clear_widgets()
        self.add_widget(layout)
        
    def go_to_menu(self, instance):
        self.manager.current = 'menu'

    def start_game(self):
        if not self.game_started:
            self.next_round()
            self.game_started = True

    def next_round(self, *args):
        # Seleccionar aleatoriamente una letra, objeto y color
        self.current_letter, object_name, color = random.choice(self.letters_colors)
        self.letter_label.text = f'Letra: {self.current_letter}'
        
        # Establecer la imagen correspondiente al objeto
        self.image.source = f'assets/images/{object_name}.png'
        
        # Reproducir el sonido correspondiente a la letra
        sound = SoundLoader.load(f'assets/sounds/{self.current_letter}1.mp3')
        if sound:
            sound.play()

    def check_color_match(self, selected_color):
    # Obtener el color correcto para la letra actual
        correct_color = [color for letter, obj, color in self.letters_colors if letter == self.current_letter][0]
        if selected_color == correct_color:
            message = f'¡Correcto! {self.current_letter} está emparejada con {correct_color.capitalize()}.'
            color = [0, 1, 0, 1]  # Verde
        else:
            message = f'Incorrecto. La letra {self.current_letter} está emparejada con {correct_color.capitalize()}.'
            color = [1, 0, 0, 1]  # Rojo
        
        # Mostrar el Popup con el mensaje y el color correspondiente
        self.show_popup(message, color)

    def show_popup(self, message, bg_color):
        popup = Popup(
            title='Resultado',
            content=Label(text=message),
            size_hint=(0.8, 0.4),
            background_color=bg_color  # Establecer el color de fondo del Popup
        )
        popup.open()

    def get_color_value(self, color_name):
        # Convertir el nombre del color a un valor RGBA
        colors = {
            'rojo': [1, 0, 0, 1],
            'verde': [0, 1, 0, 1],
            'azul': [0, 0, 1, 1],
            'amarillo': [255, 215, 0, 1]
        }
        return colors.get(color_name, [1, 1, 1, 1])  # Blanco por defecto si no se encuentra el color
   
        