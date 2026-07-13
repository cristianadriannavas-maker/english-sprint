from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import MenuScreen, BibliotecaScreen
from lesson_screen import LessonScreen


class EnglishSprint(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(BibliotecaScreen(name="biblioteca"))
        sm.add_widget(LessonScreen(name="lesson"))

        return sm


EnglishSprint().run()