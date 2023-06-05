#!/usr/bin/env python3

import ipdb 

from classes.beaches import Beaches
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.waves import Waves



#Surfboard
board1 = Surfboard('Al Merrick', 'Shortboard', 'Flyer')
board2 = Surfboard('Takayama', 'Longboard', 'Noserider')
board3 = Surfboard('Santa Cruz', 'Mid Length', 'Egg')

#surfers
surfer1 = Surfer('River', 'Ferguson', 26, 'Be better')
surfer2 = Surfer('Caz', 'Mozeleski', 28, 'Hotdogger')
surfer3 = Surfer('Guy', 'buddy', 30, 'beat it kook')

#waves
wave1 = Waves(10, 'Mean', 10, 10)
wave2 = Waves(9, 'localized', 9, 10)
wave3 = Waves(7, 'Super localized', 5, 4)
wave4 = Waves(8, 'Worst locals ever', 10, 10) 

#beaches
beach1 = Beaches('Pipeline', 'Hawaii', 10, wave1)
beach2 = Beaches('Sunset Beach', 'Hawaii', 9, wave2)
beach3 = Beaches('Velzy Land', 'Hawaii', 7, wave3)
beach4 = Beaches('Dirt Bags', 'California', 3, wave4)

print('Debugger')

ipdb.set_trace()