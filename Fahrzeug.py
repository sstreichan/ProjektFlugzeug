import json
import random
from Flughafen import Flughafen


class Fahrzeug:
    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0):
        try:
            if _name == "":
                _name = random.choice(list(self.data.keys()))

            self.name = _name
            self.speed = _speed
            self.data = self.data[_name]

            self.speed_max = int(self.data["speed"])
            self.gewicht_leer = int(self.data["leerGewicht"])
            self.gewicht_max = int(self.data["maximalGewicht"])
            self.passagiere_max = int(self.data["passagiere"])
            self.tank = int(self.data["tank"])
            self.reichweite = int(self.data["reichweite"])

            self.verbrauch = round(self.tank / self.reichweite * 100)
            self.gewicht = _gewicht
            self.passagiere = 0
            if _passagiere == -1:
                self.passagiere_einsteigen(random.randint(0, self.passagiere_max))
            else:
                self.passagiere_einsteigen(_passagiere)
            self.pos = random.choice(Flughafen.parkpos)
        except KeyError:
            print(f"Fahrzeug {_name} nicht in der Datenbank")

    def load(self, name):
        """
        Load the data from a JSON file into the `data` attribute.

        Parameters:
            name (str): The name of the JSON file to load.

        Returns:
            None
        """
        f = open(f"./data/{name}.json", "r", encoding="utf8")
        self.data = json.loads(f.read())

    def beschleunigen(self, wert):
        """
        Erhöht die aktuelle Geschwindigkeit des Flugzeugs um den angegebenen Wert.

        Parameter:
            wert (int): Der Wert, um den die Geschwindigkeit erhöht werden soll.
        """
        self.speed += wert

    def bremsen(self, wert):
        """
        Verringert die aktuelle Geschwindigkeit des Flugzeugs um den angegebenen Wert.

        Parameter:
            wert (int): Der Wert, um den die Geschwindigkeit verringert werden soll.
        """
        self.speed -= wert

    def passagiere_einsteigen(self, wert):
        """
        Erhöht die Anzahl der Passagiere und das gewicht des Flugzeugs um den angegebenen Wert.

        Parameter:
            wert (int): Die Anzahl der Passagiere, die hinzugefügt werden sollen.

        Raises:
            Exception (Ausnahme): Wenn die maximale Anzahl der Fluggäste überschritten wird.
        """
        if (
            self.passagiere + wert < self.passagiere_max
            and self.gewicht + round(wert * 81.6) < self.gewicht_max
        ):
            self.passagiere += wert
            self.gewicht += round(wert * 81.6)
        else:
            pass
            '''raise Exception(
                f"das flugzeug ist voll! {self._passagiere + wert}/{self.passagiere_max}"
            )'''

    def passagiere_aussteigen(self, wert):
        """
        Verringert die Anzahl der Passagiere und das gewicht des Flugzeugs um den angegebenen Wert.

        Parameter:
            wert (int): Die Anzahl der Passagiere, die abgezogen werden sollen.

        Raises:
            Exception (Ausnahme): Wenn die minimale Anzahl der Fluggäste überschritten wird.
        """
        if self.passagiere - wert >= 0:
            self.passagiere -= wert
            self.gewicht -= round(wert * 81.6)
        else:
            raise Exception("nicht genug passagiere im flugzeug!")

    def __str__(self):
        return (
            f"{self.name} geschwindigkeit (km/h): {self.speed}/{self.speed_max} "
            f"gewicht (kg): {self.gewicht}/{self.gewicht_max} passagiere: "
            f"{self.passagiere}/{self.passagiere_max} verbrauch(l/km): "
            f"{self.verbrauch}/100"
        )
