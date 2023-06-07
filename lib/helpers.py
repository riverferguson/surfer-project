
from rich import print 

def welcome():
    print('Welcome to Wave-Tracker')
    
    
def menu():
    print('Please select an option')
    print('1. List all names of beaches')
    print('2. List all difficult waves')
    print('3. List all surfers')
    print('4. List all surfboards')
    print('5. Find a beach by name')
    print('6. Find a difficulty of a wave by id')
    print('7. Find a surfer\'s motto by name')
    print('8. Add a new beach to our list')
    print('9. Add a new surfer')
    print('10. Add a new surfboard')
    print('11. Find most dangerous wave')
    print('12. Find safest wave')
    print('13. Find most popular beach')
    print('14. Find least popular beach')
    print('15. Exit')
    
def list_beaches():
    beaches = Beach.find_all()
    for beach in beaches:
        print(beach.name)
        
def list_waves():
    waves = Wave.find_all()
    for wave in waves:
        print(wave.difficulty)
        
def list_surfers():
    surfers = Surfer.find_all()
    for surfer in surfers:
        print(surfer.first_name)
        
def list_surfboards():
    surfboards = Surfboard.find_all()
    for surfboard in surfboards:
        print(surfboard.model)
        
def find_beach_by_name(beach):
    beach_name = Beach.find_by_name(beach)
    
    if beach_name:
        print(beach_name.location)
    else:
        raise Exception("Beach not found. Enter valid name")
    
def find_difficulty_by_id(wave_id):
    difficulty_id = Wave.find_by_id(wave_id)
    print(difficulty_id.difficulty)
    
def find_motto(first_name):
    motto = Surfer.find_by_name(first_name)
    print(motto.motto)
    
def add_new_beach():
    name = input("Enter new beach name: ")
    location = input("Enter location of new beach: ")
    popularity = input("Enter the popularity level (number between 1 & 10): ")
    wave_id = input("Enter a wave ID: ")
    surfer_id = input("Enter your surfer's ID: ")
    if (
        isinstance(name, str)
    and isinstance(location, str)
    and isinstance(popularity, int)
    and isinstance(wave_id, int)
    and isinstance(surfer_id, int)
    and len(name)
    and len(location)
    and popularity
    and wave_id
    and surfer_id
    ):
        try:
            new_beach = Beach.create(name, location, popularity, wave_id, surfer_id)
            print(new_beach)
        except Exception as error:
            print("Error creating beach: ", error)
    else:
        print("Invalid name, location, popularity, wave_id, or surfer_id")
        
def add_new_surfer():
    pass

def add_new_surfboard():
    pass
    
def find_most_dangerous_wave():
    most_dangerous = Wave.find_most_dangerous()
    print(most_dangerous.danger_level)

def find_safest_wave():
    safest_wave = Wave.find_safest_wave()
    print(safest_wave.danger_level)

def find_most_popular_beach():
    most_popular = Beach.find_most_popular()
    print(most_popular.name)

def find_lest_popular_beach():
    least_popular = Beach.find_least_popular()
    print(least_popular.name)            
        
def exit_program():
    print("Goodbye!")
    exit()
    
from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave
    