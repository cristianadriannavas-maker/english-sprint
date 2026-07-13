    import json

from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class LessonScreen(Screen):

    titulo = StringProperty("")
    frase = StringProperty("")
    traduccion = StringProperty("")
    progreso = StringProperty("1 / 1")

    numero = 0
    dataset = None

    def cargar(self, archivo, indice=0):

        with open(archivo, encoding="utf-8") as f:
            self.dataset = json.load(f)

        self.numero = indice

        self.titulo = self.dataset["video"]["title"]

        self.mostrar()

    def mostrar(self):

        item = self.dataset["sentences"][self.numero]

        self.frase = item["sentence"]

        self.traduccion = item["translation"] or "Sin traducción"

        total = len(self.dataset["sentences"])

        self.progreso = f"{self.numero+1} / {total}"

    def siguiente(self):

        if self.numero < len(self.dataset["sentences"])-1:
            self.numero += 1
            self.mostrar()

    def anterior(self):

        if self.numero > 0:
            self.numero -= 1
            self.mostrar()

    def volver(self):

        self.manager.current = "biblioteca"