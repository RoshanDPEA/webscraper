from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_string('''
<RootWidget>
    FloatLayout:
        Image:
            id: imgh
            pos: self.pos
            size_hint: None, None
            size: root.size
            allow_stretch: True
            keep_ratio: False
            source: 'background.gif'
''')

"""
class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
"""

# copy the root widget in the other screen with differnt images
class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class Window1(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

class Window2(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

class Window3(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    MyMainApp().run()
