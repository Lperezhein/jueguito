from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import random

class NumberPuzzleScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_number_puzzle()

    def create_number_puzzle(self):
        layout = GridLayout(cols=3, padding=20, spacing=10)
        self.numbers = random.sample(range(1, 9), 8)  # Números del 1 al 8 de forma aleatoria
        self.numbers.append(9)  # Agregar el espacio vacío
        random.shuffle(self.numbers)

        self.buttons = []  # Lista para mantener una referencia de los botones
        self.empty_button = None  # Variable para mantener el botón vacío

        for number in self.numbers:
            if number == 9:
                btn = Button(text='', font_size=24)  # Botón vacío sin texto
            else:
                btn = Button(text=str(number), font_size=24)
            
            btn.bind(on_release=self.move_number)
            layout.add_widget(btn)
            self.buttons.append(btn)  # Agregar botón a la lista

            if number == 9:
                self.empty_button = btn  # Establecer el botón vacío inicialmente

        # Agregar el botón "Volver al Menú"
        btn_back = Button(text='Volver al Menú', size_hint=(1, None), height=50)
        btn_back.bind(on_release=self.go_to_menu)

        layout_menu = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout_menu.add_widget(Label(text='Puzzle de Números', font_size=32))
        layout_menu.add_widget(layout)
        layout_menu.add_widget(btn_back)

        self.add_widget(layout_menu)

    def move_number(self, instance):
        # Verificar si el botón presionado puede moverse al espacio vacío
        if self.can_move(instance):
            # Intercambiar los textos de los botones
            instance_text = instance.text
            instance.text = self.empty_button.text
            self.empty_button.text = instance_text

            # Actualizar el botón vacío
            self.empty_button = instance

        # Verificar si se ha completado el puzzle
        if self.check_sequence():
            self.show_popup("¡Felicidades! Has completado el puzzle.", [0, 1, 0, 1])  # Popup verde

    def can_move(self, button):
        # Obtener la posición del botón y del botón vacío en la lista
        empty_position = self.buttons.index(self.empty_button)
        button_position = self.buttons.index(button)

        # Obtener las coordenadas (fila, columna) del botón y del botón vacío
        empty_row, empty_col = divmod(empty_position, 3)
        button_row, button_col = divmod(button_position, 3)

        # Verificar si el botón está en una posición adyacente al espacio vacío
        if (abs(empty_row - button_row) == 1 and empty_col == button_col) or \
           (abs(empty_col - button_col) == 1 and empty_row == button_row):
            return True
        else:
            return False

    def check_sequence(self):
        # Verifica si los números están en la secuencia correcta
        expected_number = 1
        for btn in self.buttons:
            if btn.text == '':
                continue  # Saltar el botón vacío
            if int(btn.text) != expected_number:
                return False
            expected_number += 1
        return True

    def go_to_menu(self, instance):
        self.manager.current = 'menu'  # Cambiar a la pantalla de menú

    def show_popup(self, message, bg_color):
        # Mostrar el Popup con el mensaje y el color correspondiente
        popup = Popup(
            title='Resultado',
            content=Label(text=message),
            size_hint=(0.8, 0.4),
            background_color=bg_color  # Establecer el color de fondo del Popup
        )
        popup.open()

