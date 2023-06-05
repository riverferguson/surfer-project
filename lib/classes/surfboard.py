from .__init__ import CONN, CURSOR

class Surfboard:
    
    def __init__(self, shaper, height, width, thickness, type):
        self.shaper = shaper
        self.height = height
        self.width = width
        self.thickness = thickness
        self.type = type 