from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from time import *
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
# I comment this because I don't know what is does ?
#from kivy.storage.dictstore import DictStore
#And this class too :3
"""
class Storage(DictStore):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.get()
"""

class WidgetExample(GridLayout):
    count = 1
    validate_text = StringProperty("Hit enter")
    count_enable = BooleanProperty(True)
    my_string = StringProperty("1")
    slider_text = StringProperty("1")
    def click_state(self,widget):
        print("toggle state:" + widget.state)
        if widget.state == "normal":
            self.count_enable = True
        if widget.state == "down":
            self.count_enable = False
    def click(self):
        print("Button click")

        if self.count_enable == False:
            self.count += 1
            self.my_string = str(self.count)
        else:
            print("Nothing")
    def switch_active(self,widget):
        print("Switch :"+ str(widget.active))

    def show_value(self,widget):
        self.slider_text = str(widget.value)
    def text_validate(self,widget):
        self.validate_text = widget.text
class PageLayoutExample(PageLayout):
    pass
class ScrollViewExample(ScrollView):
    pass
class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        for i in range(0,100):
            b1 = Button(text=str(i+1),size_hint=(.2,.2),size=(dp(50),dp(50)))
            self.add_widget(b1)
class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass

"""    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass
TheLabApp().run()