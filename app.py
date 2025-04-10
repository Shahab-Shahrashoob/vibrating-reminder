from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        layout.add_widget(Label(text="Hello"))
        layout.add_widget(Button(text="Click"))
        return layout

MyApp().run()