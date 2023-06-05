from classes.__init__ import CONN, CURSOR

class Surfboard:
    
    def __init__(self, shaper, size, model):
        self.shaper = shaper
        self.size = size
        self.model = model
        
    
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
        
    @classmethod
    def create_table(cls):
        pass
    
    @classmethod
    def create(cls):
        pass
    
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