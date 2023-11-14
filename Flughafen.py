import random

class Flughafen:
    
    def __init__(self, _name, _flugzeuge, _parkpos, _personen):
        """
        Initializes a new instance of the class.

        Parameters:
            _name (str): The name of the Airport.
            _flugzeuge (list): The list of airplanes.
            _parkpos (int): The number of parking positions.
            _personen (int): The number of people.

        Returns:
            None
        """
        self.name = _name
        self.flugzeuge = _flugzeuge
        self.parkpos = _parkpos
        self.personen = _personen
        
        
    def __str__(self):
        return f"name: {self.name} flugzeuge: {self.count_flugzeuge()} personen: {self.count_personen()}"
        
    
    def landen(self, flugzeug):
    	"""
    	Adds a given aircraft to the list of aircrafts in the airport and assigns a random parking position to the aircraft.

    	Parameters:
    	- flugzeug (Aircraft): The aircraft to be added to the list of aircrafts.

    	Returns:
    	None
    	"""

        self.flugzeuge.append(flugzeug)
        flugzeug.pos = random.choice(self.parkpos)
    
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
        pass
    
    
        
        
