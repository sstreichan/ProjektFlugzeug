import random
from Gebaeude import Gebaeude

class Flughafen(Gebaeude):
    parkpos = ["Terminal 1", "Terminal 2", "Halle 1"]
    
    def __init__(self, _name, _flugzeuge, _personen):
        """
        Initialisiert ein Flughafen-Objekt mit den angegebenen Parametern.

        Args:
            _name (str): Der Name des Flughafens.
            _flugzeuge (list): Eine Liste von Flugzeugen auf dem Flughafen.
            _personen (int): Die Gesamtanzahl der Personen auf dem Flughafen.
        """
        self.name = _name
        self.flugzeuge = _flugzeuge
        self.personen = _personen        
        
    def __str__(self):
        """
        Gibt eine formatierte Zeichenkette mit Informationen über den Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit dem Namen, der Anzahl der Flugzeuge, der Anzahl der Personen und den Parkpositionen.
        """
        return f"name: {self.name}\nFlugzeuge: {self.count_flugzeuge()}\nPersonen: {self.count_personen()}\n Parkpositionen:\n{self.get_parkPos()}"

    def landen(self, flugzeug):
        """
        Lässt ein Flugzeug auf dem Flughafen landen, weist ihm eine zufällige Parkposition zu und fügt es zur Liste der Flugzeuge hinzu.

        Args:
            flugzeug (Flugzeug): Das zu landende Flugzeug.

        Returns:
            str: Eine Meldung über die erfolgreiche Landung des Flugzeugs.
        """
        flugzeug.pos = random.choice(self.parkpos)
        self.flugzeuge.append(flugzeug)
        return f"Eine {flugzeug.name} ist gelandet."

    def start(self, flugzeug=None):
        """
        Startet ein Flugzeug vom Flughafen, entweder ein bestimmtes Flugzeug oder ein zufällig ausgewähltes.

        Args:
            flugzeug (Flugzeug, optional): Das zu startende Flugzeug. Wenn None, wird ein zufälliges Flugzeug ausgewählt.

        Returns:
            str: Eine Meldung über den erfolgreichen Start des Flugzeugs oder eine Benachrichtigung, wenn kein Flugzeug auf dem Flughafen ist.
        """
        if not self.flugzeuge:
            return "Kein Flugzeug auf dem Flughafen!"

        if flugzeug is None:
            flugzeug = random.choice(self.flugzeuge)

        self.flugzeuge.remove(flugzeug)
        return f"{flugzeug.name} ist gestartet."

    def aussteigen(self, flugzeug):
        """
        Lässt Passagiere aus einem Flugzeug aussteigen, erhöht die Anzahl der Personen auf dem Flughafen und aktualisiert die Passagierliste des Flugzeugs.

        Args:
            flugzeug (Flugzeug): Das Flugzeug, aus dem die Passagiere aussteigen sollen.

        Returns:
            str: Eine Meldung über die Anzahl der ausgestiegenen Passagiere.
        """
        result = ""
        passagiereTemp = flugzeug.passagiere
        self.personen += passagiereTemp
        flugzeug.passagiere_aussteigen(passagiereTemp)

        result = f"Es sind {passagiereTemp} ausgestiegen."
        return result
   
    
    def count_personen(self):
        """
        Zählt die Gesamtanzahl der Personen auf dem Flughafen, einschließlich der Passagiere in den Flugzeugen.

        Returns:
            int: Die Gesamtanzahl der Personen auf dem Flughafen.
        """
        personenTemp = self.personen
        for flugzeug in self.flugzeuge:
            personenTemp += flugzeug.passagiere
        return personenTemp

    def count_flugzeuge(self):
        """
        Zählt die Anzahl der Flugzeuge auf dem Flughafen.

        Returns:
            int: Die Anzahl der Flugzeuge auf dem Flughafen.
        """
        return len(self.flugzeuge)

    def get_flugzeuge(self):
        """
        Gibt eine formatierte Zeichenkette mit Informationen über alle Flugzeuge auf dem Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit Informationen über alle Flugzeuge auf dem Flughafen.
        """
        result = ""
        for flugzeug in self.flugzeuge:
            result += f"{flugzeug}\n"
        return result

    
    def get_FlugzeugeDropDown(self, text="", count=0):
        """
        Erzeugt eine Dropdown-Liste mit den Namen aller Flugzeuge auf dem Flughafen.

        Args:
            text (str): Der bisherige Text der Dropdown-Liste (default ist eine leere Zeichenkette).
            count (int): Der aktuelle Zähler für die Rekursion (default ist 0).

        Returns:
            str: Die vollständige Dropdown-Liste als Zeichenkette.
        """
        if count == len(self.flugzeuge):
            return text

        return f"<option>{self.flugzeuge[count].name}</option> {self.get_FlugzeugeDropDown(text, count+1)}"

    def get_parkPos(self):
        """
        Gibt Informationen über die Parkpositionen und die zugeordneten Flugzeuge auf dem Flughafen zurück.

        Returns:
            str: Eine formatierte Zeichenkette mit Informationen über die Parkpositionen und zugeordneten Flugzeuge auf dem Flughafen.
        """
        result = ""
        
        for pos in self.parkpos:
            result += f"{pos}:\n"
            for flugzeug in self.flugzeuge:
                if flugzeug.pos == pos:
                    result += f"\t{flugzeug.name}\n"
        return result

    def Gebaeude_reinigen(self):
        """
        Gibt eine Meldung über die Reinigung des Flughafengebäudes zurück.

        Returns:
            str: Eine Meldung über die Reinigung des Flughafengebäudes.
        """
        return f"Das Gebäude {self.name} wurde gereinigt."

        