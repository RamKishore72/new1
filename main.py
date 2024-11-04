from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Username input
        self.username_input = TextInput(hint_text='Username', multiline=False)
        layout.add_widget(self.username_input)

        # Password input
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        layout.add_widget(self.password_input)

        # Login button
        login_button = Button(text='Login')
        login_button.bind(on_release=self.login)
        layout.add_widget(login_button)

        # Add layout to screen
        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        # Dummy authentication for demonstration
        if username == "user" and password == "pass":
            self.show_popup("Login Successful", "Welcome!")
        else:
            self.show_popup("Login Failed", "Invalid credentials!")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()


class Ram(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    Ram().run()


    