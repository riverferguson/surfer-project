from .__init__ import CONN, CURSOR

class Beaches:
    
    def __init__(self, name, location, popularity, wave, surfer):
        self.name = name
        self.location = location
        self.popularity = popularity
        self.wave = wave
        self.surfer = surfer 
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('Name must be a string between 1 and 15 charcters!')
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str) and 1 <= len(location) <= 20:
            self._location = location
        else:
            raise Exception('Location must be between a string between 1 and 20 characters kook!')
        
    @property
    def wave(self):
        return self._wave
    
    @wave.setter
    def wave(self, wave):
        if isinstance(wave, Waves):
            self._wave = wave
        else:
            raise Exception
        
    @property
    def surfer(self):
        return self._surfer
    
    @surfer.setter
    def surfer(self, surfer):
        if isinstance(surfer, Surfer):
            self._wave = surfer
        else:
            raise Exception   
    
from classes.waves import Waves
from classes.surfer import Surfer 
        