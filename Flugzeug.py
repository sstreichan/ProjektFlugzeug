from Fahrzeug import Fahrzeug

class Flugzeug(Fahrzeug):
    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0
    
    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0):
        """
        Initialisiert ein Flugzeug-Objekt unter Berücksichtigung der geladenen Daten.

        Args:
            _name (str, optional): Der Name des Flugzeugs.
            _speed (int, optional): Die Geschwindigkeit des Flugzeugs.
            _passagiere (int, optional): Die Anzahl der Passagiere im Flugzeug.
            _gewicht (int, optional): Das Gewicht des Flugzeugs.

        Returns:
            None
        """
        self.load(__name__)
        super().__init__(_name, _speed, _passagiere, _gewicht)
        
        self.maxFlughoehe = int(self.data["maxFlughoehe"])
        YourClassName.anzahl_flugzeuge += 1
        YourClassName.anzahl_passagiere_gesamt += _passagiere

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
        if self.speed_max > other.speed_max: self_p += 1
        else: other_p += 1
        if self.gewicht_max > other.gewicht_max: self_p += 1
        else: other_p += 1
        if self.passagiere_max > other.passagiere_max: self_p += 1
        else: other_p += 1
        if self.reichweite > other.reichweite: self_p += 1
        else: other_p += 1
        if self.speed_max > other.speed_max: self_p += 1
        else: other_p += 1
        if self.verbrauch < other.verbrauch: self_p += 1
        else: other_p += 1

        return self_p > other_p

    def __str__(self):
        return (
            f"{super().__str__()} "
            f"max Flughöhe(m): {self.maxFlughoehe}"
            )

    def start(self):
        import time
        import pygame
        file = "sicherheitsAnweisung.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    
    def Umsteigen(self, other):
        result = ""
        
        return result