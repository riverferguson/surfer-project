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
            self._surfer = surfer
        else:
            raise Exception('A lot of beaches have surfers, be sure to add one!')   
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS beaches(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                popularity TEXT,
                wave TEXT,
                surfer TEXT
            );
        """
        )
        CONN.commit()
        
    @classmethod
    def save(cls, name, location, popularity, wave, surfer):
        beach = Beach(name, location, popularity, wave, surfer)
        CURSOR.execute(f"""
                INSERT INTO beaches(name, location, popularity, wave, surfer)
                VALUES('{beach.name}', '{beach.location}', '{beach.popularity}', '{beach.wave}', '{beach.surfer}')
        """)
        CONN.commit()
        
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("""
            SELECT * FROM beaches
            WHERE name is ?;
        """, (name, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None       
    
    @classmethod
    def find_by_id(cls):
        CURSOR.execute("""
            SELECT * FROM beaches
            WHERE id is ?;
        """, (id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[0]) if row else None
    
    @classmethod
    def update(cls, name, location, popularity):
        beach = Beach(name, location, popularity)
        CURSOR.execute("""
            UPDATE beaches
            SET name=?, location=?, popularity=?
            WHERE id = ?
        """, (beach.name, beach.location, beach.popularity, beach.id))
        CONN.commit()
    
    @classmethod
    def find_all(cls):
        CURSOR.execute("""
            SELECT * FROM beaches
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[0]) for row in rows]



from classes.waves import Waves
from classes.surfer import Surfer 
        