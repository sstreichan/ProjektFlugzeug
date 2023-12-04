import random

class Flughafen:
    parkpos = ["Terminal 1", "Terminal 2", "Halle 1"]
    
    def __init__(self, _name, _flugzeuge, _personen):
        """
        Parameters:
            _name (str): The name of the Airport.
            _flugzeuge (list): The list of airplanes.
            _personen (int): The number of people.

        Returns:
            None
        """
        self.name = _name
        self.flugzeuge = _flugzeuge
        self.personen = _personen
        
        
    def __str__(self):
        return f"name: {self.name}\nFlugzeuge: {self.count_flugzeuge()}\nPersonen: {self.count_personen()}\n Parkpositionen:\n{self.get_parkPos()}"
        
    
    def landen(self, flugzeug):
        """
    	Adds a given aircraft to the list of aircrafts in the airport and assigns a random parking position to the aircraft.

    	Parameters:
    	- flugzeug (Aircraft): The aircraft to be added to the list of aircrafts.

    	Returns:
    	None
    	"""
        flugzeug.pos = random.choice(self.parkpos)
        self.flugzeuge.append(flugzeug)
        
        return (f"Eine {flugzeug.name} landet")
    
    def start(self, flugzeug):
        """
        Removes the specified flugzeug from the list of flugzeuge and updates its position to "Luft".

        Parameters:
            flugzeug (Flugzeug): The flugzeug object to be removed.

        Returns:
            None
        """
        self.flugzeuge.remove(flugzeug)
        flugzeug.pos = "Luft"
    
    def count_personen(self):
        personenTemp = self.personen
        for flugzeug in self.flugzeuge:
            personenTemp += flugzeug.passagiere
        return personenTemp
            
    
    def count_flugzeuge(self):
        return len(self.flugzeuge)
    
    
    def get_flugzeuge(self):
        result = ""
        for flugzeug in self.flugzeuge:
            result += f"{flugzeug}\n"
        return result

    def get_parkPos(self):
        result = ""
        
        for pos in self.parkpos:
            result += f"{pos}:\n"
            for flugzeug in self.flugzeuge:
                if flugzeug.pos == pos:
                    result += f"\t{flugzeug.name}\n"
        return result
        