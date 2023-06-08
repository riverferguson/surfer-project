import re
import os 

def welcome():
    print("""
        
                _      _      _      
        )`'-.,_)`'-.,_)`'-.,_)`'-.,_
        
        'Welcome to Wave-Tracker'
        _        _      _      _      
        )`'-.,_)`'-.,_)`'-.,_)`'-.,_
        """)

    
def menu():
    print("""
        'Please select an option'
        """)
    print('1. Add a new surfer')
    print('2. List all surfers')
    print('3. List all surfboards')
    print('4. List all beaches')
    print('5. Find a difficulty of a wave by id')
    print('6. Find a surfer\'s motto by name')
    print('7. Add a new beach that you have surfed to our list')
    print('8. Find location of beach by it\'s name')
    print('9. Add a new surfboard')
    print('10. Find most dangerous wave')
    print('11. Find safest wave')
    print('12. Find most popular beach')
    print('13. Find least popular beach')
    print('14. Exit')
    
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
        print(f"{surfer.first_name} {surfer.last_name}, {surfer.age}")
        
def list_surfboards():
    surfboards = Surfboard.find_all()
    for surfboard in surfboards:
        print(surfboard.model)
        
def find_beach_by_name(beach):
    beach_name = Beach.find_by_name(beach)
    
    if beach_name:
        print(beach_name.location)
    else:
        print("Beach not found. Enter valid name")
    
def find_difficulty_by_id(wave_id):
    difficulty_id = Wave.find_by_id(wave_id)
    print(difficulty_id.difficulty)
    
def find_motto(first_name):
    motto = Surfer.find_by_name(first_name)
    print(motto.motto)
    
def add_new_beach():
    print("""
        To add a new beach we need to a name, location, popularity, a wave ID, and your surfer ID.
        """)
    name = input("Enter new beach name: ")
    location = input("Enter location of new beach: ")
    popularity = input("Enter the popularity level (number between 1 & 10): ")
    wave_id = input("Enter a wave ID (1: easy, 2: medium, 3:Hard): ")
    surfer_id = input("Enter your surfer's ID: ")
    if (
        re.match(r"^\d+" , popularity)
        and re.match(r"^\d+" , wave_id)
        and re.match(r"^\d+" , surfer_id)
    ):
        try:
            new_beach = Beach.create(name, location, int(popularity), int(wave_id), int(surfer_id))
            print(f"""
                Alright, {new_beach.name} has been added to our list!
                """)
        except Exception as error:
            print("Error creating beach: ", error)
    else:
        print("Invalid name, location, popularity, wave_id, or surfer_id")
        
def add_new_surfer():
    print("""
    To add a surfer we need to know your first name, last name, age, and a tasty motto.      
        """)
    first_name = input("Enter new surfer's first name: ")
    last_name = input("Enter new surfer's last name: ")
    age = input("Enter new surfer's age: ")
    motto = input("Enter new surfer's motto: ")
    if (
        re.match(r"^\d+" , age)
    ):
        try:
            new_surfer = Surfer.create(first_name, last_name, int(age), motto)
            print(f"""Hey, {new_surfer.first_name}, your surfer id is: {new_surfer.id}.
                """)
        except Exception as error:
            print("Error creating surfer: ", error)
    else:
        print("Invalid first name, last, age, or motto")

def add_new_surfboard():
    print("""
        To add a new surfboard, we need to know the shaper, size , the model, and your surfer ID so we know its yours! 
        """)
    shaper = input("Enter new surfboards shaper: ")
    size = input("Enter new surfboards size (shortboard, mid-length, or longboard): ")
    model = input("Enter new surfboards model: ")
    surfer_id = input("Enter surfer's id who owns this new board: ")
    if (
        isinstance(shaper, str)
        and isinstance(size, str)
        and isinstance(model, str)
        and re.match(r"^\d+" , surfer_id)
    ):
        try:
            new_surfboard = Surfboard.create(shaper, size, model, surfer_id)
            print(f"""
                Ok, your new {new_surfboard.model} has beem added to our board rack with your ID: ({new_surfboard.surfer_id}) attached.
                """)
        except Exception as error:
            print("Error creating surfboard: ", error)
    else:
        print("Invalid shaper, size, model or surfer_id")
    
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
    
def clear_terminal():
    os.system('clear')          
        
def exit_program():
    print("Goodbye!")
    exit()
    
from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave
    