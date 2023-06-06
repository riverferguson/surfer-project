from classes.__init__ import CONN, CURSOR

class Surfer:
    
    def __init__(self, first_name, last_name, age, motto, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.motto = motto
        self.id = id
        
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 15:
            self._first_name = first_name
        else:
            raise Exception('First name must be a string between 1 and 15 charcters dude!')
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 15:
            self._last_name = last_name
        else:
            raise Exception('Last name must be a string between 1 and 15 charcters buddy!') 
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 2 <= age <= 100:
            self._age = age
        else:
            raise Exception('Age must be a number between 2 and 100 bro...any older you might croak')
        
    @property
    def motto(self):
        return self._motto
    
    @motto.setter
    def motto(self, motto):
        if isinstance(motto, str) and 3 <= len(motto) <= 20:
            self._motto = motto
        else:
            raise Exception('Your motto must be a string between 3 and 20 characters guy...we dont want your life story')
        
    
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
        pass
    

    def save(self):
        CURSOR.execute("""
                INSERT INTO surfers(first_name, last_name, age, motto)
                VALUES(?, ?, ?, ?)
        """, (self.first_name, self.last_name, self.age, self.motto))
        CONN.commit()
        self.id = CURSOR.lastrowid
        
    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS surfers(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                motto TEXT
            );
        """
        )
        CONN.commit()
        
    @property
    def create(cls, first_name, last_name, age, motto):
        new_surfer = cls(first_name, last_name, age, motto)
        new_surfer.save()
        return new_surfer 
    
    @classmethod
    def find_by_name(cls):
        pass
    
    @classmethod
    def find_by_id(cls):
        pass
    

    @classmethod
    def find_all(cls):
        pass
    
        
from classes.surfboard import Surfboard 