from kivy.app import App
from kivy.uix.stacklayout import StackLayout
class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
class TheLab(App):
    pass
TheLab().run()