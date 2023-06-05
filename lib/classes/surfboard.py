from .__init__ import CONN, CURSOR

class Surfboard:
    
    def __init__(self, shaper, height, width, thickness, make):
        self.shaper = shaper
        self.height = height
        self.width = width
        self.thickness = thickness
        self.make = make 