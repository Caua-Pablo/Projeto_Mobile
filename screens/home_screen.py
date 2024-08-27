from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class AddPasswordScreen(Screen):
    pass

class SegundaTela(Screen):
    pass



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddPasswordScreen(name='segunda_tela'))
        sm.add_widget(AddPasswordScreen(name='add_password'))

        return sm

if __name__ == '__main__':
    MyApp().run()
