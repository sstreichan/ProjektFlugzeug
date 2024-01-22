self.pos = random.choice(Flughafen.parkpos)
            
''' obsolete 
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
            return f"das flugzeug ist voll! {self._passagiere + wert}/{self.passagiere_max}"

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
    '''