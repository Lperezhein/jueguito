from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from myapp.alphabet_screen import AlphabetScreen
from myapp.number_hunt_screen import NumberHuntScreen
from myapp.color_match_screen import ColorMatchScreen
from myapp.number_puzzle_screen import NumberPuzzleScreen
from myapp.solar_system_screen import SolarSystemScreen

class MenuScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        # Cargar la música de fondo
        self.music = SoundLoader.load('background_music.mp3')
        
        if self.music:
            self.music.volume = 0.2  # Volumen bajo
            self.music.loop = True
            self.music.play()  # Iniciar la reproducción de la música
        
               
        # Programar la detención de la música después de 15 segundos
        Clock.schedule_once(self.stop_music, 15)
        
        # Crear el ScreenManager y añadir todas las pantallas
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AlphabetScreen(name='alphabet'))
        sm.add_widget(NumberHuntScreen(name='number_hunt'))
        sm.add_widget(ColorMatchScreen(name='color_match'))
        sm.add_widget(NumberPuzzleScreen(name='number_puzzle'))
        sm.add_widget(SolarSystemScreen(name='solar_system'))
        
        return sm
    
    def stop_music(self, dt):
        # Detener la música cuando pase el tiempo especificado (15 segundos)
        if self.music and self.music.state == 'play':
            self.music.stop()
    
    def on_stop(self):
        # Detener la música cuando la aplicación se cierra
        if self.music:
            self.music.stop()
    
    def on_pause(self):
        # Pausar la música cuando la aplicación está en segundo plano
        if self.music and self.music.state == 'play':
            self.music.stop()
        return True
    
    def on_resume(self):
        # Reanudar la música cuando la aplicación vuelve a primer plano
        if self.music and self.music.state == 'stop':
            self.music.play()

if __name__ == '__main__':
    MyApp().run()
