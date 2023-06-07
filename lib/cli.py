from helpers import (
    welcome,
    menu,
    list_beaches,
    list_surfboards,
    list_surfers,
    list_waves,
    find_beach_by_name,
    find_beach_by_name,
    exit_program,
    find_difficulty_by_id,
    find_motto
)

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == '1':
            list_beaches()
        elif choice == '2':
            list_waves()
        elif choice == '3':
            list_surfers()
        elif choice == '4':
            list_surfboards()
        elif choice == '5':
            beach_name = input('Enter beach name and find its location: ')
            find_beach_by_name(beach_name)
        elif choice == '6':
            wave_id = input('Enter wave ID to find difficulty level: ')
            find_difficulty_by_id(wave_id)
        elif choice == '7':
            surfer_name = input('Enter surfer name to find motto: ')
            find_motto(surfer_name)
        elif choice == '20':
            exit_program
            break
        else:
            print("Invalid choice")
            
            

if __name__ == "__main__":
    main()