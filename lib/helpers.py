def welcome():
    print('Welcome to Wave-Tracker')
    
    
def menu():
    print('Please select an option')
    print('1. List all beaches')
    print('2. List all waves')
    print('3. List all surfers')
    print('4. List all surfboards')
    print('5. Find a beach by name')
    print('6. Find a wave by id')
    print('7. Find a surfer by name')
    print('8. Find a surfboard by id')
    print('9. Add a new beach to our list')
    print('10. Add a new surfboard')
    print('11. Add a new surfer')
    print('12. Add a new wave')
    print('13. Delete a broken surfboard')
    print('14. Delete a tired surfer')
    print('15. Delete a wave that is too dangerous')
    print('16. Exit')
    
def list_beaches():
    beaches = Beach.find_all()
    for beach in beaches:
        print(beach)
        
def list_waves():
    waves = Wave.find_all()
    for wave in waves:
        print(wave)
        
def list_surfers():
    surfers = Surfer.find_all()
    for surfer in surfers:
        print(surfer)
        
def list_surfboards():
    surfboards = Surfboard.find_all()
    for surfboard in surfboards:
        print(surfboard)
    
from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave
    