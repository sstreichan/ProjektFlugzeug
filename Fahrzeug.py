import json

class Fahrzeug:   

    def __init__(self, _name, _speed=0, _passagiere=0, _gewicht=0):
        #self.load()
        self.name = _name
        self.speed = _speed

        self.speed_max = int(Flugzeug.data[_name]["speed"])
        self.gewicht_leer = int(Flugzeug.data[_name]["leerGewicht"])
        self.gewicht_max = int(Flugzeug.data[_name]["maximalGewicht"])
        self.passagiere_max = int(Flugzeug.data[_name]["passagiere"])
        self.tank = int(Flugzeug.data[_name]["tank"])
        self.reichweite = int(Flugzeug.data[_name]["reichweite"])
        self.verbrauch = round(self.tank / self.reichweite * 100)
        self.gewicht = _gewicht
        self.passagiere = 0
        self.passagiere_einsteigen(_passagiere)
        self.pos = ""
        
        
    def load(self, name):
        f = open(f"{name}.json", "r")
        self.data = json.loads(f.read())
        print(self.data)

        
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
            raise Exception(
                f"das flugzeug ist voll! {self.passagiere + wert}/{self.passagiere_max}"
            )

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
        self.passagiere -= wert