import os
import json

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label


class MenuScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        boton = Button(
            text="Biblioteca"
        )

        boton.bind(on_press=self.abrir)

        layout.add_widget(boton)

        self.add_widget(layout)

    def abrir(self, instance):

        self.manager.current = "biblioteca"


class BibliotecaScreen(Screen):

    def on_enter(self):

        self.clear_widgets()

        layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        layout.add_widget(Label(
            text="Biblioteca",
            size_hint_y=None,
            height=50
        ))

        scroll = ScrollView()

        lista = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=10
        )

        lista.bind(minimum_height=lista.setter("height"))

        carpeta = "data/datasets"

        if os.path.exists(carpeta):

            for archivo in sorted(os.listdir(carpeta)):

                if archivo.endswith(".json"):

                    ruta = os.path.join(carpeta, archivo)

                    with open(ruta, encoding="utf8") as f:

                        data = json.load(f)

                    boton = Button(
                        text=data["video"]["title"],
                        size_hint_y=None,
                        height=70
                    )

                    boton.bind(
                        on_press=lambda x, r=ruta: self.abrir_video(r)
                    )

                    lista.add_widget(boton)

        scroll.add_widget(lista)

        layout.add_widget(scroll)

        self.add_widget(layout)

    def abrir_video(self, ruta):

        pantalla = self.manager.get_screen("lesson")

        pantalla.cargar(ruta, 0)

        self.manager.current = "lesson"