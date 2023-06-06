from classes.__init__ import CONN, CURSOR

class Wave:
    
    def __init__(self, difficulty, local_attitude, danger_level, popularity, id=None):
        self.difficulty = difficulty
        self.local_attitude = local_attitude
        self.danger_level = danger_level
        self.popularity = popularity
        self.id = id
        
    
    @property
    def difficulty(self):
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, difficulty):
        if isinstance(difficulty, int) and 1 <= difficulty <= 10:
            self._difficulty = difficulty
        else:
            raise Exception('Difficulty must be between a number between 1 and 10...stay humble dude')
        
    @property
    def local_attitude(self):
        return self._local_attitude
    
    @local_attitude.setter
    def local_attitude(self, local_attitude):
        if isinstance(local_attitude, str) and 4 <= len(local_attitude) <= 20:
            self._local_attitude = local_attitude
        else:
            raise Exception('Local attitude must be a string between 4 and 20 charcacters...share the beach man!')
        
    @property
    def danger_level(self):
        return self._danger_level
    
    @danger_level.setter
    def danger_level(self, danger_level):
        if isinstance(danger_level, int) and 1 <= danger_level <= 10:
            self._danger_level = danger_level
        else:
            raise Exception('Danger level must be a number between 1 and 10...be safe out there fellas')
    
    @property
    def popularity(self):
        return self._popularity
    
    @popularity.setter
    def popularity(self, popularity):
        if isinstance(popularity, int) and 1 <= popularity <= 10:
            self._popularity = popularity
        else:
            raise Exception('Popularity must be a number between 1 and 10 bro!')   
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS waves(
                id INTEGER PRIMARY KEY,
                difficulty INTEGER,
                local_attitude TEXT,
                danger_level INTEGER,
                popularity INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, difficulty, local_attitude, danger_level, popularity):
        new_wave = cls(difficulty, local_attitude, danger_level, popularity)
        new_wave.save()
        return new_wave
    
    def save(self):
        CURSOR.execute(f"""
                INSERT INTO waves(difficulty, local_attitude, danger_level, popularity)
                VALUES(?, ?, ?, ?);
        """, (self.difficulty, self.local_attitude, self.danger_level, self.popularity))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
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