from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

# Access Android's Vibrator service
Context = autoclass('android.content.Context')
Activity = autoclass('org.kivy.android.PythonActivity').mActivity
Vibrator = Activity.getSystemService(Context.VIBRATOR_SERVICE)

class MyApp(App):
    def build(self):
        btn = Button(text="Press to Vibrate")
        btn.bind(on_press=self.vibrate)
        return btn

    def vibrate(self, instance):
        Vibrator.vibrate(500)  # Vibrates for 500 milliseconds

MyApp().run()