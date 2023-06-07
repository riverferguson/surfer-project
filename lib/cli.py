from helpers import (
    welcome,
    menu,
    list_beaches,
    list_surfboards,
    list_surfers,
    list_waves,
    find_beach_by_name,
    find_beach_by_name,
    find_difficulty_by_id,
    find_motto,
    add_new_beach,
    add_new_surfer,
    add_new_surfboard,
    find_most_dangerous_wave,
    find_safest_wave,
    find_most_popular_beach,
    find_lest_popular_beach,
    exit_program
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
        elif choice == '8':
            new_beach = input('Enter new beach: ')
            add_new_beach(new_beach)
        elif choice == '9':
            pass
        elif choice == '10':
            pass
        elif choice == '11':
            find_most_dangerous_wave()
        elif choice == '12':
            find_safest_wave()
        elif choice == '13':
            find_most_popular_beach()
        elif choice == '14':
            find_lest_popular_beach()
        elif choice == '15':
            exit_program
            break
        else:
            print("Invalid choice")
            
            

if __name__ == "__main__":
    main()