from simple_chalk import chalk, green, red, magenta, blue, cyan

from helpers import (
    welcome,
    menu,
    list_beaches,
    list_surfboards,
    list_surfers,
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
    clear_terminal,
    exit_program
)

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == '1':
            clear_terminal()
            add_new_surfer()
        elif choice == '2':
            clear_terminal()
            list_surfers()
        elif choice == '3':
            clear_terminal()
            list_surfboards()
        elif choice == '4':
            clear_terminal()
            list_beaches()
        elif choice == '5':
            wave_id = input(chalk.magenta.bold('Enter wave ID to find difficulty level: '))
            clear_terminal()
            find_difficulty_by_id(wave_id)
        elif choice == '6':
            surfer_name = input(chalk.cyan('Enter surfer name to find motto: '))
            clear_terminal()
            find_motto(surfer_name)
        elif choice == '7':
            clear_terminal()
            add_new_beach()
        elif choice == '8':
            beach_name = input('Enter beach name and find its location: ')
            clear_terminal()
            find_beach_by_name(beach_name)
        elif choice == '9':
            clear_terminal()
            add_new_surfboard()
        elif choice == '10':
            clear_terminal()
            find_most_dangerous_wave()
        elif choice == '11':
            clear_terminal()
            find_safest_wave()
        elif choice == '12':
            clear_terminal()
            find_most_popular_beach()
        elif choice == '13':
            clear_terminal()
            find_lest_popular_beach()
        elif choice == '14':
            exit_program
            break
        else:
            print("Invalid choice")
            
            

if __name__ == "__main__":
    main()