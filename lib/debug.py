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

# Surfer.find_by_name()
# Beach.find_by_name()

# Surfboard.find_all()
# Surfer.find_all()
# Wave.find_all()



# Surfboard.find_by_id()
# Surfer.find_by_id()
# Wave.find_by_id()
# Beach.find_by_id()

#surfers
surfer1 = Surfer.create('River', 'Ferguson', 26, 'Get Pitted')
surfer2 = Surfer.create('Caz', 'Mozeleski', 28, 'Hotdogger')
surfer3 = Surfer.create('Guy', 'buddy', 30, 'beat it kook')
surfer4 = Surfer.create('Buddy', 'Guy', 22, "Hey Guyyy")
surfer5 = Surfer.create('Craig', 'Dude', 22, "Stoked")

#Surfboard
board1 = Surfboard.create('Al Merrick', 'Shortboard', 'Flyer', surfer1.id)
board2 = Surfboard.create('Takayama', 'Longboard', 'Noserider', surfer2.id)
board3 = Surfboard.create('Santa Cruz', 'Mid Length', 'Egg', surfer3.id)
board4 = Surfboard.create('Lost', 'Mid Length', 'Mayhem', surfer3.id)
board5 = Surfboard.create('Arakawa', 'Shortboard', 'Carver', surfer5.id)
board6 = Surfboard.create('Tokoro', 'Longboard', 'Spooner', surfer4.id)
board7 = Surfboard.create('Aipa', 'Shortboard', 'Islander', surfer1.id)

#waves
wave1 = Wave.create(10, 'Mean', 10, 10)
wave2 = Wave.create(9, 'localized', 9, 10)
wave3 = Wave.create(7, 'Super localized', 5, 4)
wave4 = Wave.create(8, 'Worst locals ever', 10, 10) 

#beaches
beach1 = Beach.create('Pipeline', 'Hawaii', 10, wave1.id, surfer1.id)
beach2 = Beach.create('Sunset Beach', 'Hawaii', 9, wave2.id, surfer5.id)
beach3 = Beach.create('Velzy Land', 'Hawaii', 7, wave3.id, surfer3.id)
beach4 = Beach.create('Dirt Bags', 'California', 3, wave4.id, surfer2.id)

print('Debugger')



#ipdb.set_trace()