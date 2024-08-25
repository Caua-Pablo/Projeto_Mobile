import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.add_password import AddPasswordScreen


sys.path.append(os.path.dirname(os.path.abspath(__file__)))



from kivy.core.window import Window

# Defina o tamanho da janela para simular um dispositivo móvel
Window.size = (360, 640)  # Dimensões típicas para um dispositivo móvel em modo retrato



class ScreenManagement(ScreenManager):
    pass

class PasswordManagerApp(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddPasswordScreen(name='add_password'))
        return sm

if __name__ == '__main__':
    PasswordManagerApp().run()


