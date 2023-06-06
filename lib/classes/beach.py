#!/usr/bin/env python3

class Beach:
    
    def __init__(self, name, location, popularity, wave_id, surfer_id, id=None):
        self.name = name
        self.location = location
        self.popularity = popularity
        self.wave_id = wave_id
        self.surfer_id = surfer_id
        self.id = id 
        
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
        return Wave.find_by_id(self.wave_id)
    
    @wave.setter
    def wave(self, wave_id):
        if isinstance(wave_id, int) and wave_id > 0 and Wave.find_by_id(self.wave_id):
            self._wave_id = wave_id
        else:
            raise Exception('ID has to be an existing integer greater than 0')
        
    @property
    def surfer(self):
        return Surfer.find_by_id(self.surfer_id)
    
    @surfer.setter
    def surfer(self, surfer_id):
        if isinstance(surfer_id, int) and surfer_id > 0 and Surfer.find_by_id(self.surfer_id):
            self._surfer_id = surfer_id
        else:
            raise Exception('ID has to be an existing integer greater than 0')   
    
    def update(self):
        CURSOR.execute(
            """
            UPDATE beaches
            SET name = ?, location = ?, popularity = ?, wave_id = ?, surfer_id = ?
            WHERE id = ?
            """,
            (
                self.name,
                self.location,
                self.popularity,
                self.wave_id,
                self.surfer_id,
            ),
        )
        CONN.commit()
        return type(self).find_by_id(self.id)
    
    def save(self):
        CURSOR.execute("""
                INSERT INTO beaches(name, location, popularity, wave_id, surfer_id)
                VALUES(?, ?, ?, ?, ?)
        """, (self.name, self.location, self.popularity, self.wave_id, self.surfer_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        
    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM beaches
            WHERE id = ?;
            """,
            (self.id,),
        )
        CONN.commit()
    
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS beaches(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                popularity TEXT,
                wave_id INTEGER,
                surfer_id INTEGER,
                FOREIGN KEY (wave_id) REFERENCES waves(id),
                FOREIGN KEY (surfer_id) REFERENCES surfers(id)
            );
        """
        )
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS beaches;
        """
        )
        CONN.commit()
        
    @classmethod
    def create(cls, name, location, popularity, wave_id, surfer_id):
        new_beach = cls(name, location, popularity, wave_id, surfer_id)
        new_beach.save()
        return new_beach
    
    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("""
            SELECT * FROM beaches
            WHERE name is ?;
        """, (name, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None       
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("""
            SELECT * FROM beaches
            WHERE id is ?;
        """, (id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None
    
    @classmethod
    def find_all(cls):
        CURSOR.execute("""
            SELECT * FROM beaches
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]



from classes.__init__ import CONN, CURSOR
from classes.wave import Wave
from classes.surfer import Surfer 