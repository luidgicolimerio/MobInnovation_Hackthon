# App principal
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from tinydb import TinyDB

db = TinyDB('database.json')

class MyBoxLayout(BoxLayout):
    
    def cadastrar(self, *args):
        user_text = self.ids.user_input.text
        password_text = self.ids.password_input.text
        db.insert(
            {
              'user': user_text,
              'password': password_text
              }
        )

class MainApp(App):  
    def build(self):
        return MyBoxLayout()
    
MainApp().run()