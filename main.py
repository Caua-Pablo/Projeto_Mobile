from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class HomeScreen(Screen):
    pass

class Menu_Opcoes(Screen):
    pass

class Visualizador_Senhas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.credenciais = []

    def adicionar_credenciais(self, nome, usuario, senha, notas):
        # Adiciona a nova credencial à lista
        self.credenciais.append((nome, usuario, senha, notas))
        # Atualiza a visualização
        self.atualizar_credenciais()

    def atualizar_credenciais(self):
        # Limpa o layout antes de adicionar novos botões
        self.ids.credenciais_box.clear_widgets()
        # Adiciona um botão para cada credencial salva
        for credencial in self.credenciais:
            nome, usuario, senha, notas = credencial
            button = Button(text=nome, size_hint_y=None, height=40)
            # Ao clicar no botão, mostrar as credenciais
            button.bind(on_press=lambda x, n=nome, u=usuario, s=senha, nt=notas: self.mostrar_credenciais(n, u, s, nt))
            self.ids.credenciais_box.add_widget(button)

    def mostrar_credenciais(self, nome, usuario, senha, notas):
        # Exibe um popup com os detalhes da credencial
        popup_content = f"Nome: {nome}\nUsuário: {usuario}\nSenha: {senha}\nNotas: {notas}"
        popup = Popup(title="Detalhes da Credencial", content=Label(text=popup_content), size_hint=(0.8, 0.5))
        popup.open()

class AddCredencial(Screen):
    def on_pre_enter(self, *args):
        # Limpa os campos de entrada quando a tela é ativada
        self.ids.nome_input.text = ''
        self.ids.usuario_input.text = ''
        self.ids.senha_input.text = ''
        self.ids.notas_input.text = ''

    def salvar_credencial(self, nome, usuario, senha, notas):
        # Obtém a instância do aplicativo
        app = App.get_running_app()
        # Adiciona a nova credencial à lista de credenciais da tela de visualização
        app.root.get_screen('Visualizador_Senhas_contas').adicionar_credenciais(nome, usuario, senha, notas)
        # Volta para a tela de visualização de senhas
        self.manager.current = 'Visualizador_Senhas_contas'

class MyScreenManager(ScreenManager):
    pass

class CredenciaisApp(App):
    def build(self):
        # Definir a resolução e a cor de fundo
        Window.size = (360, 640)
        Window.clearcolor = (19/255, 33/255, 69/255, 1)  # Fundo azul

        # Carregar o arquivo KV
        Builder.load_file('home_screen.kv')

        # Instanciar o ScreenManager
        sm = MyScreenManager()

        # Adicionar as telas ao ScreenManager
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Menu_Opcoes(name='menu_opcoes_escolha'))
        sm.add_widget(Visualizador_Senhas(name='Visualizador_Senhas_contas'))
        sm.add_widget(AddCredencial(name='add_credencial_senha'))

        return sm

if __name__ == '__main__':
    CredenciaisApp().run()
