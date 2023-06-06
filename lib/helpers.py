import re 

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
    print('16. Find most dangerous wave')
    print('17. Find safest wave')
    print('18. Find most popular beach')
    print('19. Find least popular beach')
    print('20. Exit')
    
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
        
def find_beach_by_name():
    name = input("Enter the name of the beach: ")
    if len(name).trim() and re.match(r"^[a-zA-Z ]+$", name) and name.title():
        beach = Beach.find_by_name(name.title())
        print(beach) if beach else print("No beach found")
    else:
        print("Invalid name")
        
def exit_program():
    print("Goodbye!")
    exit()
    
from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave
    