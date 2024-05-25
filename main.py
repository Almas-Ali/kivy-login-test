from typing import Dict

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from models import authenticate_user, create_user, get_user

session: Dict[str, str] = {"username": ""}


class LoginScreen(Screen):
    username: ObjectProperty = ObjectProperty("")
    password: ObjectProperty = ObjectProperty("")

    def login_user(self) -> None:
        if authenticate_user(self.username.text, self.password.text):
            print("Login success")
            session["username"] = self.username.text

            self.username.text = ""
            self.password.text = ""

            self.manager.transition.direction = "down"
            self.manager.current = "home"

        else:
            print("Login failed")

            box = BoxLayout(orientation="vertical")
            box.add_widget(Label(text="Invalid username or password"))
            box.add_widget(Button(text="Close", on_press=lambda x: popup.dismiss(), size_hint=(1, None), height=40))

            popup = Popup(
                title="Login failed",
                content=box,
                size_hint=(None, None),
                size=(300, 300),
            )
            popup.open()


class RegistrationScreen(Screen):
    email: ObjectProperty = ObjectProperty("")
    username: ObjectProperty = ObjectProperty("")
    password: ObjectProperty = ObjectProperty("")

    def register_user(self) -> None:
        if get_user(self.username.text):
            print("User already exists")
            return

        create_user(self.email.text, self.username.text, self.password.text)

        self.email.text = ""
        self.username.text = ""
        self.password.text = ""

        self.manager.transition.direction = "down"
        self.manager.current = "login"


class HomeScreen(Screen):
    username = ObjectProperty("")
    email = ObjectProperty("")

    def on_pre_enter(self) -> None:
        if session["username"]:
            user = get_user(session["username"])
            self.username = user.username
            self.email = user.email
        else:
            self.username = "Guest"
            self.email = ""

    def logout(self) -> None:
        session["username"] = ""
        self.manager.transition.direction = "up"
        self.manager.current = "login"


class MainApp(App):
    title: str = "Login App"
    # title.pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def build(self) -> Builder:
        return Builder.load_file("design.kv")


if __name__ == "__main__":
    MainApp().run()
