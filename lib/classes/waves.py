from .__init__ import CONN, CURSOR

class Waves:
    
    def __init__(self, difficulty, local_attitude, danger_level):
        self.difficulty = difficulty
        self.local_attitude = local_attitude
        self.danger_level = danger_level
        
    
    @property
    def difficulty(self):
        return self._difficulty
    
    @difficulty.setter
    def difficulty(self, difficulty):
        if isinstance(difficulty, int) and 1 <= len(difficulty) <= 10:
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
        if isinstance(danger_level, int) and 1 <= len(danger_level) <= 10:
            self._danger_level = danger_level
        else:
            raise Exception('Danger level must be a number between 1 and 10...be safe out there fellas')
        
        