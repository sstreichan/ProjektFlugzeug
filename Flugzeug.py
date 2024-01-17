from Fahrzeug import Fahrzeug
from Utilities import *
import random
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
        self.data = loadJSON(__name__)
        super().__init__(_name, _speed, _passagiere, _gewicht)
        
        self.maxFlughoehe = int(self.data["maxFlughoehe"])
        Flugzeug.anzahl_flugzeuge += 1
        Flugzeug.anzahl_passagiere_gesamt += _passagiere
        
        self.flugnummer = random.randint(100000, 999999)
        self.abflugzeit = abflugzeit
        self.ankunftzeit = ankunftzeit
        self.fluggesellschaft = self.get_Fluggesellschaft()
        
        
    def get_Fluggesellschaft(self):
        Fluggesellschaften = ["SkyLink Airways", "Horizon Wings",
            "CelestialJet",
            "AeroVista Airlines",
            "StarLift Air",
            "CloudSail Airlines",
            "BlueSky Express",
            "SolarWings International",
            "VelocityAir",
            "NovaJet Airways"
        ]
        return random.choice(Fluggesellschaften)

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