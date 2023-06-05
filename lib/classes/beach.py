from classes.__init__ import CONN, CURSOR

class Beach:
    
    def __init__(self, name, location, popularity, wave, surfer, id=None):
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
            raise Exception('Most beaches tend to have waves grom')
        
    @property
    def surfer(self):
        return self._surfer
    
    @surfer.setter
    def surfer(self, surfer):
        if isinstance(surfer, Surfer):
            self._wave = surfer
        else:
            raise Exception('A lot of beaches have surfers, be sure to add one!')   
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS beaches(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                popularity TEXT
            );
        """
        )
        CONN.commit()
        
    @classmethod
    def create(cls, name, location, popularity):
        beach = Beach(name, location, popularity)
        CURSOR.execute(f"""
                INSERT INTO beaches(name, location, popularity)
                VALUES('{beach.name}', '{beach.location}', '{beach.popularity}')
        """)
        
    
    @classmethod
    def find_by_name(cls):
        pass
    
    @classmethod
    def find_by_id(cls):
        pass
    
    @classmethod
    def update(cls):
        pass
    
    @classmethod
    def find_all(cls):
        pass



from classes.waves import Waves
from classes.surfer import Surfer 
        