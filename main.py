from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from tinydb import TinyDB

db = TinyDB('users.json')
KV = '''
ScreenManager:
    MenuScreen:
    FormLoginScreen:

<TopBar@MDTopAppBar>:
    title: "Mob Innovation"
    left_action_items: [["menu", lambda x: x]]
<MenuScreen>:
    name: 'menu'
    MDFloatLayout:
        TopBar:
            pos_hint: {"center_y": 0.95}    
        MDLabel:
            text: 'Mobian'
            pos_hint: {"center_y": .5}
            halign: "center"
<FormLoginScreen>:
    name: 'login'
    MDFloatLayout:
        MDIconButton:
            icon: "racing-helmet"
            pos_hint: {"center_x": .5, "center_y": .8}
            icon_size: '75sp'
        MDLabel:
            text: 'Mobian'
            pos_hint: {"center_y": .7}
            halign: "center"
        MDTextField:
            id: user_input
            hint_text: 'User:'
            size_hint_x: .7
            pos_hint: {"center_x": .5, "center_y": .6}
        MDTextField:
            id: password_input
            hint_text: 'Password:'
            size_hint_x: .7
            pos_hint: {"center_x": .5, "center_y": .5}
        MDRaisedButton:
            text: 'Sign Up'
            pos_hint: {"center_x": .5, "center_y": .35}
            size_hint_x: .4
            on_press: root.cadastrar()
            on_release: app.root.current = 'menu'  # Alterna para a tela 'menu'

<MenuScreen>:
    MDFloatLayout:
        MDLabel:
            text: 'Mobian'
            pos_hint: {"center_y": .5}
            halign: "center"
'''

class MenuScreen(Screen):
    pass

class FormLoginScreen(Screen):
    def cadastrar(self, *args):
        user_text = self.ids.user_input.text
        password_text = self.ids.password_input.text
        db.insert(
            {
              'user': user_text,
              'password': password_text
              }
        )

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

    def on_start(self):
        # Define a tela inicial como FormLoginScreen
        self.root.current = 'login'

if __name__ == '__main__':
    MyApp().run()
