from Fahrzeug import Fahrzeug

class Flugzeug(Fahrzeug):
    """
        Args:
            _name (str): The name of the vehicle. random vehicle is chosen if empty.
            _speed (int): The speed of the object. Defaults to 0.
            _passagiere (int): The number of passengers. Defaults to 0. -1 For Random.
            _gewicht (int): The weight of the object. Defaults to 0.
        Raises:
            KeyError: If the name of the vehicle is not found in the database.
    """
    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0

    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0, flugnummer="", abflugzeit="", ankunftzeit="", fluggesellschaft=""):
        self.load(__name__)
        super().__init__(_name, _speed, _passagiere, _gewicht)
        
        self.maxFlughoehe = int(self.data["maxFlughoehe"])
        Flugzeug.anzahl_flugzeuge += 1
        Flugzeug.anzahl_passagiere_gesamt += _passagiere
        
        self.flugnummer = flugnummer
        self.abflugzeit = abflugzeit
        self.ankunftzeit = ankunftzeit
        self.fluggesellschaft = fluggesellschaft

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