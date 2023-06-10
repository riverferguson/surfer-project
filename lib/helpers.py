import re
import os
from simple_chalk import chalk, green, red, magenta, blue, cyan

def welcome():
    print(chalk.cyan("""
        
                _      _      _      
        )`'-.,_)`'-.,_)`'-.,_)`'-.,_
        
        'Welcome to Wave-Tracker'
        _        _      _      _      
        )`'-.,_)`'-.,_)`'-.,_)`'-.,_
        """))

    
def menu():
    print(chalk.red("""
        'Please select an option'
        """))
    print('1. Add a new surfer')
    print('2. List all surfers')
    print('3. List all surfboards')
    print('4. List all beaches')
    print('5. Find a difficulty of a wave by id')
    print('6. Find a surfer\'s motto by name')
    print('7. Add a beach that you have surfed to our list')
    print('8. Find location of beach by it\'s name')
    print('9. Add a new surfboard')
    print('10. Find most dangerous wave')
    print('11. Find safest wave')
    print('12. Find most popular beach')
    print('13. Find least popular beach')
    print('14. Show beaches surfed by surfer\'s ID')
    print('15. Exit')
    
def list_beaches():
    beaches = Beach.find_all()
    for beach in beaches:
        print(chalk.cyan(beach.name))
        
def list_waves():
    waves = Wave.find_all()
    for wave in waves:
        print(wave.difficulty)
        
def list_surfers():
    surfers = Surfer.find_all()
    for surfer in surfers:
        print(chalk.cyan(f"{surfer.first_name} {surfer.last_name}, {surfer.age}"))
        
def list_surfboards():
    surfboards = Surfboard.find_all()
    for surfboard in surfboards:
        print(chalk.cyan(f'{surfboard.shaper} + {surfboard.model}, {surfboard.size}'))
        
def find_beach_by_name(beach):
    beach_name = Beach.find_by_name(beach)
    
    if beach_name:
        print(chalk.cyan(beach_name.location))
    else:
        print("Beach not found. Enter valid name")
    
def find_difficulty_by_id(wave_id):
    difficulty_id = Wave.find_by_id(wave_id)
    print(chalk.cyan(difficulty_id.difficulty))
    
def find_motto(first_name):
    motto = Surfer.find_by_name(first_name)
    print(chalk.cyan(motto.motto))
    
def add_new_beach():
    print(chalk.cyan("""
        To add a new beach we need to a name, location, popularity, a wave ID, and your surfer ID.
        """))
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
            print(chalk.cyan(f"""
                Alright, {new_beach.name} has been added to our list!
                """))
        except Exception as error:
            print("Error creating beach: ", error)
    else:
        print("Invalid name, location, popularity, wave_id, or surfer_id")
        
def add_new_surfer():
    print(chalk.cyan("""
    To add a surfer we need to know your first name, last name, age, and a tasty motto.      
        """))
    first_name = input("Enter new surfer's first name: ")
    last_name = input("Enter new surfer's last name: ")
    age = input("Enter new surfer's age: ")
    motto = input("Enter new surfer's motto: ")
    if (
        re.match(r"^\d+" , age)
    ):
        try:
            new_surfer = Surfer.create(first_name, last_name, int(age), motto)
            print(chalk.cyan(f"""Hey, {new_surfer.first_name}, your surfer id is: {new_surfer.id}.
                """))
        except Exception as error:
            print("Error creating surfer: ", error)
    else:
        print("Invalid first name, last, age, or motto")

def add_new_surfboard():
    print(chalk.cyan("""
        To add a new surfboard, we need to know the shaper, size , the model, and your surfer ID so we know its yours! 
        """))
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
            print(chalk.cyan(f"""
                Ok, your new {new_surfboard.model} has been added to our board rack with your ID: ({new_surfboard.surfer_id}) attached.
                """))
        except Exception as error:
            print("Error creating surfboard: ", error)
    else:
        print("Invalid shaper, size, model or surfer_id")
    
def find_most_dangerous_wave():
    most_dangerous = Wave.find_most_dangerous()
    print(chalk.cyan(f'Local Attitude: {most_dangerous.local_attitude}'))
    print(chalk.cyan(f'Danger Level: {most_dangerous.danger_level}'))

def find_safest_wave():
    safest_wave = Wave.find_safest_wave()
    print(chalk.cyan(f'Local Attitude: {safest_wave.local_attitude}'))
    print(chalk.cyan(f'Danger Level: {safest_wave.danger_level}'))

def find_most_popular_beach():
    most_popular = Beach.find_most_popular()
    print(chalk.cyan(most_popular.name))

def find_lest_popular_beach():
    least_popular = Beach.find_least_popular()
    print(chalk.cyan(least_popular.name))
    
def list_beaches_surfed():
    beaches = Beach.find_all()
    for beach in beaches:
        print(chalk.cyan(f'{beach.name} was surfed by surfer ID: {beach.surfer_id}'))
    
def clear_terminal():
    os.system('clear')          
        
def exit_program():
    print("Goodbye!")
    exit()
    
from classes.beach import Beach
from classes.surfboard import Surfboard
from classes.surfer import Surfer
from classes.wave import Wave
    