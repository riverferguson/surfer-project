from classes.__init__ import CONN, CURSOR

class Surfboard:
    
    def __init__(self, shaper, size, model, surfer_id, id=None):
        self.shaper = shaper
        self.size = size
        self.model = model
        self.surfer_id = surfer_id
        self.id = id 
        
    
    @property
    def shaper(self):
        return self._shaper
    
    @shaper.setter
    def shaper(self, shaper):
        if isinstance(shaper, str) and 1 <= len(shaper) <= 15:
            self._shaper = shaper
        else:
            raise Exception('Shaper must be a string between 1 and 15 characters you barney!')
        
    @property
    def size(self):
        return self._size 
    
    @size.setter
    def size(self, size):
        if isinstance(size, str) and 4 <= len(size) <= 14:
            self._size = size
        else:
            raise Exception("Size of your board must be a str between 4 and 14...otherwise its not a surfboard")
        
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        if isinstance(model, str) and 1 <= len(model) <= 15:
            self._model = model
        else:
            raise Exception('Model must be a string between 1 and 15 characters hoale')
        
    @property
    def popularity(self):
        return self._popularity
    
    @popularity.setter
    def popularity(self, popularity):
        if isinstance(popularity, int) and 1 <= popularity <= 10:
            self._popularity = popularity
        else:
            raise Exception('Popularity must be a number between 1 and 10 bro!')
        
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
        pass
    
    def save(self):
        CURSOR.execute("""
                INSERT INTO surfboards(shaper, size, model, surfer_id)
                VALUES(?, ?, ?, ?)
        """, (self.shaper, self.size, self.model, self.surfer_id))
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
                CREATE TABLE IF NOT EXISTS surfboards(
                    id INTEGER PRIMARY KEY,
                    shaper TEXT,
                    size TEXT,
                    model TEXT,
                    surfer_id INTEGER
                );
        """)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS surfboards;
        """
        )
        CONN.commit()
        
    @classmethod
    def create(cls, shaper, size, model, surfer_id):
        new_surfboard = cls(shaper, size, model, surfer_id)
        new_surfboard.save()
        return new_surfboard
        
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("""
            SELECT * FROM surfboards
            WHERE id is ?;
        """, (id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None

    @classmethod
    def find_all(cls):
        CURSOR.execute("""
            SELECT * FROM surfboards
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]
    
    
from classes.surfer import Surfer