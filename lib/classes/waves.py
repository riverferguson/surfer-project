from .__init__ import CONN, CURSOR

class Waves:
    
    def __init__(self, difficulty, local_attitude, danger_level):
        self.difficulty = difficulty
        self.local_attitude = local_attitude
        self.danger_level = danger_level
        