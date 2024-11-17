from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import secrets
import string
import hashlib
import pyperclip
from kivy.core.clipboard import Clipboard
from kivy.properties import BooleanProperty, StringProperty





# Configuração da janela
Window.size = (360, 640)
Window.clearcolor = (19/255, 33/255, 69/255, 1)  # Fundo azul

# Função para gerar senha
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


def copiar_para_area_de_transferencia(texto):
    pyperclip.copy(texto)  # Copia o texto para a área de transferência
    print("Texto copiado para a área de transferência.")  # Para depuração, pode remover essa linha depois



       # Função para copiar senha gerada
    def copiar_senha_gerada(self):
        copiar_para_area_de_transferencia(self.senha_gerada)

    # Função para copiar a senha criptografada
    def copiar_senha_criptografada(self):
        try:
            if self.senha_criptografada:
                # Copia a senha criptografada para a área de transferência
                pyperclip.copy(self.senha_criptografada)
                print(f"Senha criptografada copiada: {self.senha_criptografada}")
            else:
                print("Senha não está definida.")
        except Exception as e:
            print(f"Erro ao copiar a senha: {e}")




# Função para criptografar a senha gerada
def criptografar_senha(senha):
    hash_obj = hashlib.sha256(senha.encode())
    senha_criptografada = hash_obj.hexdigest()
    return senha_criptografada

# Tela inicial
class HomeScreen(Screen):
    pass

# Menu de opções
class Menu_Opcoes(Screen):
    pass

# Tela do gerador de senhas
class GeradorSenhasScreen(Screen):
    senha_gerada = StringProperty("")  # Senha gerada
    senha_criptografada = StringProperty("")  # Senha criptografada (se necessário)
    hash_visivel = BooleanProperty(False)  # Controla a visibilidade do hash


    def copiar_senha(self):
        senha = self.senha_gerada  # Usando a senha gerada da propriedade
        Clipboard.copy(senha)
        self.ids.feedback_label.text = f'Senha copiada: {senha}'  # Feedback visual para o usuário
        print("Senha copiada!")

    def gerar_nova_senha(self, tamanho=12):
            senha = gerar_senha(tamanho)
            self.senha_gerada = senha
            self.senha_criptografada = criptografar_senha(senha)

    def alternar_visibilidade_hash(self):
        # Alterna a visibilidade do hash
        self.hash_visivel = not self.hash_visivel




    def copiar_senha_criptografada(self):
        try:
            if self.senha_criptografada:
                pyperclip.copy(self.senha_criptografada)
                print(f"Senha criptografada copiada: {self.senha_criptografada}")
            else:
                print("Senha não está definida.")
        except Exception as e:
            print(f"Erro ao copiar a senha: {e}")


# Tela para visualizar senhas
class Visualizador_Senhas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.credenciais = []

    def adicionar_credenciais(self, nome, usuario, senha, notas):
        self.credenciais.append((nome, usuario, senha, notas))
        self.atualizar_credenciais()

    def atualizar_credenciais(self):
        self.ids.credenciais_box.clear_widgets()
        for index, credencial in enumerate(self.credenciais):
            nome, usuario, senha, notas = credencial
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            view_button = Button(text=nome, size_hint_x=0.8)
            view_button.bind(on_press=lambda x, n=nome, u=usuario, s=senha, nt=notas: self.mostrar_credenciais(n, u, s, nt))
            delete_button = Button(text="Excluir", size_hint_x=0.2)
            delete_button.bind(on_press=lambda x, i=index: self.excluir_credencial(i))
            box.add_widget(view_button)
            box.add_widget(delete_button)
            self.ids.credenciais_box.add_widget(box)

    def mostrar_credenciais(self, nome, usuario, senha, notas):
        popup_content = f"Nome: {nome}\nUsuário: {usuario}\nSenha: {senha}\nNotas: {notas}"
        popup = Popup(title="Detalhes da Credencial", content=Label(text=popup_content), size_hint=(0.8, 0.5))
        popup.open()

    def excluir_credencial(self, index):
        del self.credenciais[index]
        self.atualizar_credenciais()

# Tela para adicionar credencial
class AddCredencial(Screen):
    def on_pre_enter(self, *args):
        self.ids.nome_input.text = ''
        self.ids.usuario_input.text = ''
        self.ids.senha_input.text = ''
        self.ids.notas_input.text = ''

    def salvar_credencial(self, nome, usuario, senha, notas):
        app = App.get_running_app()
        app.root.get_screen('Visualizador_Senhas_contas').adicionar_credenciais(nome, usuario, senha, notas)
        self.manager.current = 'Visualizador_Senhas_contas'

# Gerenciador de telas
class MyScreenManager(ScreenManager):
    pass

# Aplicativo principal
class CredenciaisApp(App):
    def build(self):
        Builder.load_file('home_screen.kv')
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Menu_Opcoes(name='menu_opcoes_escolha'))
        sm.add_widget(Visualizador_Senhas(name='Visualizador_Senhas_contas'))
        sm.add_widget(AddCredencial(name='add_credencial_senha'))
        sm.add_widget(GeradorSenhasScreen(name="gerador_senhas"))
        return sm

if __name__ == '__main__':
    CredenciaisApp().run()
