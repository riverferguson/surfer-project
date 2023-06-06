#!/usr/bin/env python3
from classes.__init__ import CONN, CURSOR
import ipdb 

from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave



#Surfboard
board1 = Surfboard('Al Merrick', 'Shortboard', 'Flyer')
board2 = Surfboard('Takayama', 'Longboard', 'Noserider')
board3 = Surfboard('Santa Cruz', 'Mid Length', 'Egg')

#surfers
surfer1 = Surfer('River', 'Ferguson', 26, 'Be better')
surfer2 = Surfer('Caz', 'Mozeleski', 28, 'Hotdogger')
surfer3 = Surfer('Guy', 'buddy', 30, 'beat it kook')

#waves
wave1 = Wave.create(10, 'Mean', 10, 10)
wave2 = Wave.create(9, 'localized', 9, 10)
wave3 = Wave.create(7, 'Super localized', 5, 4)
wave4 = Wave.create(8, 'Worst locals ever', 10, 10) 

#beaches
beach1 = Beach('Pipeline', 'Hawaii', 10, wave1, surfer1)
beach2 = Beach('Sunset Beach', 'Hawaii', 9, wave2, surfer1)
beach3 = Beach('Velzy Land', 'Hawaii', 7, wave3, surfer3)
beach4 = Beach('Dirt Bags', 'California', 3, wave4, surfer2)


print('Debugger')

# Waves.create_table()
# Waves.save(9, 'localized', 6, 7)
#Waves.create_table()

print('done')
# Surfer.create_table()
# Beach.create_table()
# wave1.save()
# surfer1.save()
# Surfboard.create_table()


#ipdb.set_trace()