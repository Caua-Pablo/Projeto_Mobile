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

class Menu_Opcoes(Screen):
    def save_password(self, password):
        # Função que salva a senha no banco de dados SQLite
        conn = sqlite3.connect('database/passwords.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (password) VALUES (?)', (password,))
        conn.commit()
        conn.close()
        print(f"Senha '{password}' salva com sucesso!")

