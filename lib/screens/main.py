from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Important(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
    name_input = ObjectProperty()
    text_label = ObjectProperty()
    age_input = ObjectProperty()
    def ecrire(self, source):
        if self.name_input.text != "" and self.age_input.text != "":
            self.text_label.color = (0,0,0,1)
            self.text_label.text ="Vous vous appelez {}\n et vous avez {} ans.".format(self.name_input.text, self.age_input.text)
        else:
            self.text_label.color = (1,0,0,1)
            self.text_label.text = "Alerte: Renseignez toutes vos info !"

class MyApp(App):
    pass

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')
MyApp().run()