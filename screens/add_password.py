"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
"""

from kivy.uix.screenmanager import Screen

class AddPasswordScreen(Screen):
    pass


from kivy.uix.screenmanager import Screen
import sqlite3

class AddPasswordScreen(Screen):
    def save_password(self, password):
        # Função que salva a senha no banco de dados SQLite
        conn = sqlite3.connect('database/passwords.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (password) VALUES (?)', (password,))
        conn.commit()
        conn.close()
        print(f"Senha '{password}' salva com sucesso!")

"""
class AddPasswordScreen(Screen):
    def __init__(self, **kwargs):
        super(AddPasswordScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        self.password_input = TextInput(hint_text="Digite sua senha")
        btn_save = Button(text='Salvar Senha')
        btn_save.bind(on_press=self.save_password)
        
        layout.add_widget(self.password_input)
        layout.add_widget(btn_save)
        self.add_widget(layout)
    
    def save_password(self, instance):
        password = self.password_input.text
        print(f'Senha salva: {password}')
        # Aqui você pode adicionar a lógica de salvar a senha no banco de dados
"""