from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
import re

# KV layout definition
kv = '''
# Login screen layout
<MaterialTextInput>:
    name: "login"
    FloatLayout:
        MDTextField:
            id: username_input
            hint_text: "Email"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .65}
            mode: "rectangle"
            helper_text: "Enter a valid email"
            helper_text_mode: "on_focus"
            error: False  # To control error highlighting

        MDTextField:
            id: password_input
            hint_text: "Password"
            font_size: "20dp"
            icon_right: "eye-off"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .5}
            mode: "rectangle"
            password: True
            hint_text_color: (1, 1, 1, 1)
            helper_text: "Password required"
            helper_text_mode: "on_focus"
            error: False  # To control error highlighting

        # Checkbox to toggle password visibility
        BoxLayout:
            spacing: dp(5)
            size_hint: .85, None
            pos_hint: {"center_x": .5, "center_y": .38}
            height: "30dp"
            MDCheckbox:
                id: my_checkbox
                size_hint: None, None
                size: dp(30), dp(30)
                on_press:
                    password_input.password = not password_input.password
            MDLabel:
                text: "Show password"
                size_hint_y: None
                height: dp(30)
                theme_text_color: "Secondary"

        # Sign in and Sign up buttons
        BoxLayout:
            orientation: "horizontal"
            size_hint: .85, None
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .3}
            spacing: dp(10)

            MDFlatButton:
                text: "SIGN IN"
                font_size: "22dp"
                on_release:
                    app.validation()
                    app.password()
                    app.switch_to_dashboard()
                md_bg_color: 0.1, 0.7, 0.3, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)

            MDFlatButton:
                text: "SIGN UP"
                font_size: "22dp"
                on_release:
                    app.switch_to_registred()  # Ensure proper indentation
                md_bg_color: 0.7, 0.3, 0.1, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)

# Dashboard screen layout
<Dashboard>:
    name: "dashboard"
    FloatLayout:
        MDLabel:
            text: "Welcome to the Dashboard"
            font_style: "H5"
            halign: "center"
            size_hint: None, None
            size: "280dp", "50dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            theme_text_color: "Secondary"

# Registered screen layout
<registred>:
    name: "registred"
    FloatLayout:
        MDTextField:
            id: email_input
            hint_text: "Email"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .85}
            mode: "rectangle"
            helper_text: "Enter a valid email"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: firstname_input
            hint_text: "First Name"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .71}
            mode: "rectangle"
            helper_text: "Enter a valid first name"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: lastname_input
            hint_text: "Last Name"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .57}
            mode: "rectangle"
            helper_text: "Enter a valid last name"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: username_input
            hint_text: "Username"
            font_size: "20dp"
            icon_right: "account"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .43}
            mode: "rectangle"
            helper_text: "Enter a valid username"
            helper_text_mode: "on_focus"
            error: False

        MDTextField:
            id: password_input
            hint_text: "Password"
            font_size: "20dp"
            icon_right: "eye-off"
            size_hint_x: .85
            pos_hint: {"center_x": .5, "center_y": .29}
            mode: "rectangle"
            password: True
            hint_text_color: (1, 1, 1, 1)
            helper_text: "Password required"
            helper_text_mode: "on_focus"
            error: False

        # Checkbox to toggle password visibility
        BoxLayout:
            spacing: dp(5)
            size_hint: .85, None
            pos_hint: {"center_x": .5, "center_y": .18}
            height: "30dp"
            MDCheckbox:
                id: my_checkbox
                size_hint: None, None
                size: dp(30), dp(30)
                on_press:
                    password_input.password = not password_input.password
            MDLabel:
                text: "Show password"
                size_hint_y: None
                height: dp(30)
                theme_text_color: "Secondary"

        # Sign up and Sign in buttons
        BoxLayout:
            orientation: "horizontal"
            size_hint: .85, None
            height: "50dp"
            pos_hint: {"center_x": .5, "center_y": .09}
            spacing: dp(10)

            MDFlatButton:
                text: "SIGN UP"
                font_size: "22dp"
                on_release:
                    app.switch_to_login()  # Switch back to login screen
                md_bg_color: 0.1, 0.7, 0.3, 1
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                size_hint: 0.45, None
                height: dp(50)
'''

class MaterialTextInput(Screen):
    """Login screen logic"""
    pass

class Dashboard(Screen):
    """Dashboard screen logic"""
    pass

class registred(Screen):
    """Registered screen logic"""
    pass

class Ram(MDApp):
    def build(self):
        """Build and return the ScreenManager with all screens"""
        self.theme_cls.theme_style = "Dark"  # Set the theme style

        # Create ScreenManager
        sm = ScreenManager()

        # Add screens to the manager
        sm.add_widget(MaterialTextInput(name="login"))
        sm.add_widget(Dashboard(name="dashboard"))
        sm.add_widget(registred(name="registred"))

        return sm  # Return ScreenManager as root

    def validation(self):
        email = self.root.get_screen("login").ids.username_input.text
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_regex, email):
            self.root.get_screen("login").ids.username_input.helper_text = ""
            self.root.get_screen("login").ids.username_input.error = False
            print("Valid email")
            return True
        else:
            self.root.get_screen("login").ids.username_input.helper_text = "Invalid email"
            self.root.get_screen("login").ids.username_input.error = True
            print("Invalid email")
            return False

    def password(self):
        password = self.root.get_screen("login").ids.password_input.text
        if password == "":
            self.root.get_screen("login").ids.password_input.helper_text = "Invalid Password"
            self.root.get_screen("login").ids.password_input.error = True
            print("Invalid password")
            return False
        else:
            self.root.get_screen("login").ids.password_input.helper_text = ""
            self.root.get_screen("login").ids.password_input.error = False
            print("Valid password")
            return True

    def switch_to_dashboard(self):
        email = self.root.get_screen("login").ids.username_input.text
        password = self.root.get_screen("login").ids.password_input.text
        if email == "ramkishore86384@gmail.com" and password == "ramkishore123":
            self.root.current = "dashboard"  # Switch to dashboard screen
            print("Login successful")
        else:
            print("Invalid credentials")

    def switch_to_registred(self):
        self.root.current = "registred"  # Switch to the registered screen

    def switch_to_login(self):
        self.root.current = "login"  # Switch to the login screen
        # Reset all fields and errors
        self.root.get_screen("login").ids.username_input.text = ""
        self.root.get_screen("login").ids.password_input.text = ""
        self.root.get_screen("login").ids.username_input.helper_text = ""
        self.root.get_screen("login").ids.username_input.error = False
        self.root.get_screen("login").ids.password_input.helper_text = ""
        self.root.get_screen("login").ids.password_input.error = False

Builder.load_string(kv)

if __name__ == "__main__":
    Ram().run()
