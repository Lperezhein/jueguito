from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader


class PlanetInfoPopup(Popup):
    def __init__(self, planet_name, planet_desc, planet_sound, **kwargs):
        super().__init__(**kwargs)
        self.title = planet_name
        self.size_hint = (None, None)
        self.size = (400, 300)
        self.content = BoxLayout(orientation='vertical')
        self.content.add_widget(Label(text=planet_desc, size_hint_y=0.9))
        
        close_button = Button(text='Cerrar', size_hint_y=0.1)
        close_button.bind(on_release=self.dismiss)
        self.content.add_widget(close_button)
        
        self.planet_sound = SoundLoader.load(planet_sound)
        if self.planet_sound:
            self.planet_sound.volume = 0.3  # Volumen bajo para los sonidos de planetas

    def open(self):
        super().open()
        if self.planet_sound:
            self.planet_sound.play()


class SolarSystemScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text='Exploración del Sistema Solar', font_size=32)
        layout.add_widget(label)
        
        planet_buttons = GridLayout(cols=2, padding=20, spacing=20, size_hint_y=None)
        planet_buttons.bind(minimum_height=planet_buttons.setter('height'))
        
        planets = [
            ('Sol', 'El Sol es la estrella central del sistema solar.', 'assets/sounds/sol.mp3'),
            ('Mercurio', 'Mercurio es el planeta más cercano al Sol.', 'assets/sounds/mercurio.mp3'),
            ('Venus', 'Venus es conocido como el planeta gemelo de la Tierra.', 'assets/sounds/venus.mp3'),
            ('Tierra', 'La Tierra es el único planeta conocido que alberga vida.', 'assets/sounds/tierra.mp3'),
            ('Marte', 'Marte es conocido como el planeta rojo debido a su color característico.', 'assets/sounds/marte.mp3'),
            ('Júpiter', 'Júpiter es el planeta más grande del sistema solar.', 'assets/sounds/jupiter.mp3'),
            ('Saturno', 'Saturno es conocido por sus impresionantes anillos.', 'assets/sounds/saturno.mp3'),
            ('Urano', 'Urano es conocido por su inclinación axial única.', 'assets/sounds/urano.mp3'),
            ('Neptuno', 'Neptuno es el último planeta del sistema solar.', 'assets/sounds/neptuno.mp3'),
            ('Luna', 'La Luna es el satélite natural de la Tierra.', 'assets/sounds/luna.mp3')
        ]
        
        for planet_name, planet_desc, planet_sound in planets:
            btn = Button(text=planet_name, size_hint_y=None, height='60dp')
            btn.planet_name = planet_name
            btn.planet_description = planet_desc
            btn.planet_sound = planet_sound
            btn.bind(on_release=self.show_planet_info)
            planet_buttons.add_widget(btn)
        
        layout.add_widget(planet_buttons)
        
        back_button = Button(text='Volver al Menú', size_hint=(1, None), height=50)
        back_button.bind(on_release=self.go_to_menu)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def show_planet_info(self, instance):
        planet_name = instance.planet_name
        planet_desc = instance.planet_description
        planet_sound = instance.planet_sound
        
        # Crear y mostrar el Popup con la información y sonido del planeta
        popup = PlanetInfoPopup(planet_name=planet_name, planet_desc=planet_desc, planet_sound=planet_sound, title='Información del Planeta')
        popup.open()
    
    def go_to_menu(self, instance):
        self.manager.current = 'menu'
