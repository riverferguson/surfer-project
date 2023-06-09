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
        
    def update(self):
        CURSOR.execute(
            """
            UPDATE waves
            SET difficulty = ?, local_attitude = ?, danger_level = ?, popularity = ?
            WHERE id = ?
            """,
            (
                self.difficulty,
                self.local_attitude,
                self.danger_level,
                self.popularity,
            ),
        )
        CONN.commit()
        return type(self).find_by_id(self.id)
    
    def save(self):
        CURSOR.execute(f"""
                INSERT INTO waves(difficulty, local_attitude, danger_level, popularity)
                VALUES(?, ?, ?, ?);
        """, (self.difficulty, self.local_attitude, self.danger_level, self.popularity))
        CONN.commit()
        self.id = CURSOR.lastrowid
        
    def delete(self):
        CURSOR.execute(
            """
            DELETE FROM waves
            WHERE id = ?;
            """,
            (self.id,),
        )
        CONN.commit()    
    
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
    def drop_table(cls):
        CURSOR.execute(
            """
            DROP TABLE IF EXISTS waves;
        """
        )
        CONN.commit()
    
    @classmethod
    def create(cls, difficulty, local_attitude, danger_level, popularity):
        new_wave = cls(difficulty, local_attitude, danger_level, popularity)
        new_wave.save()
        return new_wave
    
    @classmethod
    def find_by_difficulty(cls, difficulty):
        CURSOR.execute("""
            SELECT * FROM waves
            WHERE difficulty is ?;
        """, (difficulty, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute("""
            SELECT * FROM waves
            WHERE id is ?;
        """, (id, ))
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None
        
    @classmethod
    def find_all(cls):
        CURSOR.execute("""
            SELECT * FROM waves
        """)
        rows = CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]
    
    @classmethod
    def find_most_dangerous(cls):
        CURSOR.execute(
            """
            SELECT * FROM waves
            ORDER by waves.danger_level DESC
            """
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0])
    
    @classmethod
    def find_safest_wave(cls):
        CURSOR.execute(
            """
            SELECT * FROM waves
            ORDER by waves.danger_level ASC
            """
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) 