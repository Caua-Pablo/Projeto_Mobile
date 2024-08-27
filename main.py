from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder


# Definir as telas
class HomeScreen(Screen):
    pass

class AddPasswordScreen(Screen):
    pass

class SegundaTela(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        # Definir a resolução e a cor de fundo
        Window.size = (360, 640)
        Window.clearcolor = (19/255, 33/255, 69/255, 1)  # Fundo azul
        Builder.load_file('home_screen.kv')



        

        # Instanciar o ScreenManager
        sm = MyScreenManager()

        # Adicionar as telas ao ScreenManager
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddPasswordScreen(name='add_password'))
        sm.add_widget(SegundaTela(name='segunda_tela'))
        return sm

if __name__ == '__main__':
    MyApp().run()




       
