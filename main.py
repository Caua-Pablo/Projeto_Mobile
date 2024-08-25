import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# Definindo a tela inicial (HomeScreen)
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        btn_add_password = Button(text='Adicionar Senha')
        btn_add_password.bind(on_press=self.add_password)
        
        layout.add_widget(btn_add_password)
        self.add_widget(layout)
    
    def add_password(self, instance):
        # Aqui você poderia mudar para outra tela, como a de adicionar senha
        print("Navegar para a tela de adicionar senha")
        
# Gerenciador de telas
class ScreenManagement(ScreenManager):
    pass

# Aplicativo principal
class PasswordManagerApp(App):
    def build(self):
        sm = ScreenManagement()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    PasswordManagerApp().run()
