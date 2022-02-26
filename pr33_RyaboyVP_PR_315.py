from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):
        s=Scatter()
        fl=FloatLayout(size=(400,600))
        s.add_widget(fl)
        fl.add_widget(Button(
            text="Это первая кнопка",
            font_size=25,
            on_press=self.btn_press,
            background_color=[1,.5,0,1],
            background_normal='',
            size_hint=(.5, .25),
            pos=(300, 120)));
        fl.add_widget(Button(
            text="Это вторая кнопка",
            font_size=25,
            on_press=self.btn_press,
            background_color=[1,2,0,2],
            size_hint=(.5, .25),
            pos=(300, 320)));
        s.bind(center=fl.setter('center'))
        return s
    def btn_press(self, instance):
        instance.text='Я нажата'

if __name__=="__main__":
    myApp().run()
