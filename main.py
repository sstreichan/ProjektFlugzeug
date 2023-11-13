import json

"""1) Eine Klasse definieren (Klassendiagramm) 2) Implementierung:
 3 Objektattribute und 2 Klassenattribute

 2) Mindestens 2 Operatoren überladen (+, größer)

3) Business erstellen: Objekte erzeugen und "testen".
Muss: gut kommentieren, docstring benutzen, so arbeiten, dass die Codierung weiter verwendet werden kann"""


class Flugzeug:
    """
    Klasse zum Verwalten von Flugzeugen
    Parameter: 
        geschwindigkeit, name, anzahl_passagiere, gewicht
    """

    anzahl_flugzeuge = 0  # Klassenvariablen
    anzahl_passagiere_gesamt = 0

    def __init__(self, _tempo, name, _passagiere, _gewicht):
        # Objektvariablen
        self.name = name
        self.tempo = _tempo
        self.passagiere = _passagiere
        #self.passagiere_max = _passagiere_max
        self.gewicht = _gewicht
        #Flugzeug.anzahl_flugzeuge += 1
        #Flugzeug.anzahl_passagiere_gesamt += _passagiere
        
        # JSON-Datei laden
        with open('flugzeuge.json', 'r', encoding='utf-8') as json_file:
            flugzeuge = json.load(json_file)
            for Flugzeug in flugzeuge:
                if Flugzeug.Name == name:
                    print(Flugzeug)


    def beschleunigen(self, wert):
        self.tempo += wert

    def bremsen(self, wert):
        self.tempo -= wert

    def passagiere_einsteigen(self, wert):
        if self.passagiere_max < self.passagiere + wert:
            self.passagiere += wert
        else:
            raise("das flugzeug ist voll!")

    def passagiere_aussteigen(self, wert):
        self.passagiere -= wert

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
        vergleicht ob das Flugzeug schneller ist
        Parameter:
            Class Flugzeug, Class Flugzeug
        return:
            bool
        """
        return self.tempo > other.tempo
    
    def __str__(self):
        return f"{self.name} geschwindigkeit: {self.tempo} gewicht: {self.gewicht}"
    
    
    

Boeing = Flugzeug(300, "Boeing737", 400, 41140)
Airbus = Flugzeug(400, "Airbus380", 350, 560000)

print(Boeing)

print(Boeing.tempo)
Boeing.beschleunigen(200)
print(Boeing.tempo)

print(Boeing + Airbus)
print(Airbus - Boeing)

if Boeing > Airbus:
    print("Boeing beste")
else:
    print("Airbus beste")

print(Flugzeug.anzahl_flugzeuge)
print(Flugzeug.anzahl_passagiere_gesamt)
