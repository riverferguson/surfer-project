#!/usr/bin/env python3
from classes.__init__ import CONN, CURSOR
import ipdb 

from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave

Surfer.drop_table()
Surfboard.drop_table()
Wave.drop_table()
Beach.drop_table()

Surfer.create_table()
Surfboard.create_table()
Wave.create_table()
Beach.create_table()



#surfers
surfer1 = Surfer.create('River', 'Ferguson', 26, 'Get Pitted')
surfer2 = Surfer.create('Caz', 'Mozeleski', 28, 'Hotdogger')
surfer3 = Surfer.create('Guy', 'buddy', 30, 'beat it kook')
surfer4 = Surfer.create('Buddy', 'Guy', 22, "Hey Guyyy")
surfer5 = Surfer.create('Craig', 'Dude', 22, "Stoked")

#Surfboard
board1 = Surfboard.create('Al Merrick', 'Shortboard', 'Flyer', surfer1)
board2 = Surfboard.create('Takayama', 'Longboard', 'Noserider', surfer2)
board3 = Surfboard.create('Santa Cruz', 'Mid Length', 'Egg', surfer3)
board4 = Surfboard.create('Lost', 'Mid Length', 'Mayhem', surfer3)
board5 = Surfboard.create('Arakawa', 'Shortboard', 'Carver', surfer5)
board6 = Surfboard.create('Tokoro', 'Longboard', 'Spooner', surfer4)
board7 = Surfboard.create('Aipa', 'Shortboard', 'Islander', surfer1)

#waves
wave1 = Wave.create(10, 'Mean', 10, 10)
wave2 = Wave.create(9, 'localized', 9, 10)
wave3 = Wave.create(7, 'Super localized', 5, 4)
wave4 = Wave.create(8, 'Worst locals ever', 10, 10) 

#beaches
beach1 = Beach.create('Pipeline', 'Hawaii', 10, wave1, surfer1)
beach2 = Beach.create('Sunset Beach', 'Hawaii', 9, wave2, surfer1)
beach3 = Beach.create('Velzy Land', 'Hawaii', 7, wave3, surfer3)
beach4 = Beach.create('Dirt Bags', 'California', 3, wave4, surfer2)


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