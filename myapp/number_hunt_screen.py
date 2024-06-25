# number_hunt_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random

class NumberHuntScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_number = 1
        self.create_layout()
        self.create_number_hunt_grid()
        
    def create_layout(self):
        # Crear un layout vertical para contener la cuadrícula y el botón de reinicio
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Crear el contenedor para la cuadrícula de números
        self.grid_container = BoxLayout()
        
        # Crear el botón de "Jugar de Nuevo"
        self.restart_button = Button(
            text='Jugar de Nuevo', 
            size_hint=(None, None), 
            size=(200, 50),
            background_normal='',  # Eliminar fondo predeterminado
            background_color=(0.2, 0.6, 0.8, 1),  # Color de fondo (azul claro)
            color=(1, 1, 1, 1)  # Color del texto (blanco)
        )
        self.restart_button.bind(on_release=self.restart_game)
        
        # Añadir el contenedor de la cuadrícula y el botón al layout principal
        main_layout.add_widget(self.grid_container)
        main_layout.add_widget(self.restart_button)
        
        self.add_widget(main_layout)

    def create_number_hunt_grid(self):
        self.numbers = list(range(1, 21))  # Números del 1 al 20
        random.shuffle(self.numbers)  # Mezcla los números aleatoriamente al inicio
        
        layout = GridLayout(cols=5, padding=20, spacing=10)
        for number in self.numbers:
            btn = Button(text=str(number), font_size=24, size_hint=(None, None), size=(100, 100))
            btn.bind(on_release=self.check_number)
            layout.add_widget(btn)

        self.grid_container.clear_widgets()  # Limpia widgets existentes antes de agregar la nueva grilla
        self.grid_container.add_widget(layout)  # Añade la nueva grilla al contenedor

    def check_number(self, instance):
        number = int(instance.text)
        if number == self.next_number:
            instance.background_color = (0, 1, 0, 1)  # Verde si es correcto
            self.next_number += 1
            if self.next_number > 20:
                self.next_number = 1
                random.shuffle(self.numbers)
                Clock.schedule_once(lambda dt: self.create_number_hunt_grid(), 1)  # Nueva cuadrícula después de 1 segundo
        else:
            instance.background_color = (1, 0, 0, 1)  # Rojo si es incorrecto

    def restart_game(self, instance):
        self.next_number = 1  # Reiniciar el próximo número a 1
        self.create_number_hunt_grid()  # Crear una nueva cuadrícula de números
