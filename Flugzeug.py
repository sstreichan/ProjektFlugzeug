from FlugzeugData import get_flugzeuge
from Fahrzeug import Fahrzeug

class Flugzeug(Fahrzeug):
    """
    Klasse zum Verwalten von Flugzeugen
    Parameter:
        geschwindigkeit, name, anzahl_passagiere, gewicht
    """

    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0
    data = None

    def __init__(self, _name, _speed=0, _passagiere=0, _gewicht=0):
        """
        Initialisiert eine neue Instanz der Klasse Flugzeug.

        Args:
            _name (str): Der Name des Flugzeugs.
            _speed (int): Die aktuelle Geschwindigkeit des Flugzeugs.
            _passagiere (int): Die Anzahl der Passagiere, die im Flugzeug sind.
            _gewicht (int): Das Gewicht der ladung des Flugzeugs.

        Erzeugt:
            KeyError: Wenn der Name des Flugzeugs nicht in der Datenbank gefunden wird.
        """

        if Flugzeug.data is None:
            #with open(f"{dir_path}\\flugzeuge.json", "r", encoding="utf-8") as jsonfile:
            #    Flugzeug.data = json.load(jsonfile)
            Flugzeug.data = get_flugzeuge()

        try:
            # Objektvariablen
            #self.maxFlughoehe = 
            Flugzeug.anzahl_flugzeuge += 1
            Flugzeug.anzahl_passagiere_gesamt += _passagiere
        except KeyError:
            print(f"Flugzeug {_name} nicht in der Datenbank")

    def __add__(self, other):
        """
        addiert Gewicht der Flugzeuge
        Parameter:
            Class Flugzeug, Class Flugzeug
        return:
            Summe Gewicht der Flugzeuge
        """
        return self.gewicht + other.gewicht

    def __sub__(self, other):
        """
        subtrahiert Passagiere der Flugzeuge
        Parameter:
            Class Flugzeug, Class Flugzeug
        return:
            Differenz Anzahl der Passagiere in den Flugzeugen
        """
        return self.gewicht - other.gewicht

    def __gt__(self, other):
        """
        vergleicht ob das Flugzeug besser ist
        Parameter:
            Class Flugzeug, Class Flugzeug
        return:
            bool
        """
        self_p = 0
        other_p = 0
        if self.speed_max > other.speed_max:
            self_p += 1
        else:
            other_p += 1
        if self.gewicht_max > other.gewicht_max:
            self_p += 1
        else:
            other_p += 1
        if self.passagiere_max > other.passagiere_max:
            self_p += 1
        else:
            other_p += 1
        if self.reichweite > other.reichweite:
            self_p += 1
        else:
            other_p += 1
        if self.speed_max > other.speed_max:
            self_p += 1
        else:
            other_p += 1
        if self.verbrauch < other.verbrauch:
            self_p += 1
        else:
            other_p += 1

        return self_p > other_p

    def __str__(self):
        return f"{self.name} geschwindigkeit (km/h): {self.speed}/{self.speed_max} gewicht (kg): {self.gewicht}/{self.gewicht_max} passagiere: {self.passagiere}/{self.passagiere_max} verbrauch(l/km): {self.verbrauch}/100"

    def start(self):
        import time
        import pygame
        file = "sicherheitsAnweisung.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
            
 