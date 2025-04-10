from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from jnius import autoclass

# Access Android Vibration Service
Context = autoclass('android.content.Context')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity
Vibrator = Activity.getSystemService(Context.VIBRATOR_SERVICE)

class SpeechTimerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.input_field = TextInput(hint_text="Enter interval in minutes")
        self.layout.add_widget(self.input_field)
        
        self.start_button = Button(text="Start Timer")
        self.start_button.bind(on_press=self.start_timer)
        self.layout.add_widget(self.start_button)
        
        return self.layout

    def start_timer(self, instance):
        interval = int(self.input_field.text) * 60  # Convert minutes to seconds
        Clock.schedule_interval(self.vibrate_alert, interval)

    def vibrate_alert(self, dt):
        Vibrator.vibrate(500)  # Vibrate for 500ms

SpeechTimerApp().run()