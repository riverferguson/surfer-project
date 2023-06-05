#!/usr/bin/env python3
from classes.__init__ import CONN, CURSOR
import ipdb 

from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.waves import Waves



#Surfboard
board1 = Surfboard('Al Merrick', 'Shortboard', 'Flyer')
board2 = Surfboard('Takayama', 'Longboard', 'Noserider')
board3 = Surfboard('Santa Cruz', 'Mid Length', 'Egg')

#surfers
surfer1 = Surfer('River', 'Ferguson', 26, 'Be better', board1)
surfer2 = Surfer('Caz', 'Mozeleski', 28, 'Hotdogger', board2)
surfer3 = Surfer('Guy', 'buddy', 30, 'beat it kook', board3)

#waves
wave1 = Waves(10, 'Mean', 10, 10)
wave2 = Waves(9, 'localized', 9, 10)
wave3 = Waves(7, 'Super localized', 5, 4)
wave4 = Waves(8, 'Worst locals ever', 10, 10) 

#beaches
beach1 = Beach('Pipeline', 'Hawaii', 10, wave1, surfer1)
beach2 = Beach('Sunset Beach', 'Hawaii', 9, wave2, surfer1)
beach3 = Beach('Velzy Land', 'Hawaii', 7, wave3, surfer3)
beach4 = Beach('Dirt Bags', 'California', 3, wave4, surfer2)

print('Debugger')

Beach.create_table()
Beach.create("Morro Bay", "California", 6, wave1, surfer1)
# Surfboard.create_table()
# Surfer.create_table()
# Waves.create_table()


#ipdb.set_trace()