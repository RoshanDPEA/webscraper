from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window

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

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
class TestApp(App):
    def build(self):
        return RootWidget(size_hint=(None,None), size=Window.size)

if __name__ == '__main__':
    TestApp().run()
