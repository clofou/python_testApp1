from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from dbFunction import login, register

class Important(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
    email_input = ObjectProperty()
    text_label = ObjectProperty()
    pass_input = ObjectProperty()
    def ecrire(self, source):
        if self.email_input.text != "" and self.pass_input.text != "":
            isLogin = register(self.email_input.text, self.pass_input.text)
            self.text_label.color = (0,0,0,1)
            if isLogin:
                self.text_label.text ="Vous êtes dejà enrégisté !"
            else:
                self.text_label.color = (1,0,0,1)
                self.text_label.text = "Vous n'avez pas de compte !"
        else:
            self.text_label.color = (1,0,0,1)
            self.text_label.text = "Alerte: Renseignez toutes vos info !"

class MyApp(App):
    pass

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
MyApp().run()