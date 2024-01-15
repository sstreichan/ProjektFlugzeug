from Fahrzeug import Fahrzeug

class Flugzeug(Fahrzeug):
    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0
    
    def __init__(self, _name="", _speed=0, _passagiere=0, _gewicht=0, flugnummer="", abflugzeit="", ankunftzeit="", fluggesellschaft=""):
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
        Flugzeug.anzahl_flugzeuge += 1
        Flugzeug.anzahl_passagiere_gesamt += _passagiere
        
        self.flugnummer = flugnummer
        self.abflugzeit = abflugzeit
        self.ankunftzeit = ankunftzeit
        self.fluggesellschaft = fluggesellschaft

    
    ''' obsolete
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
    '''
    def __str__(self):
        """
        Gibt eine formatierte Zeichenkette mit Informationen über das Flugzeug zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit dem Namen, der Geschwindigkeit, der Anzahl der Passagiere, dem Gewicht und der maximalen Flughöhe.
        """
        return (
            f"{super().__str__()} "
            f"max Flughöhe(m): {self.maxFlughoehe}"
        )

    ''' obsolete    
    def Umsteigen(self, other):
        result = ""        
        return result
    '''