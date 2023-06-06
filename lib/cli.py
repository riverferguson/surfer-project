from helpers import (
    welcome,
    menu,
    list_beaches,
    list_surfboards,
    list_surfers,
    list_waves,
    find_beach_by_name,
    exit_program
)

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == '1':
            list_beaches
        elif choice == '2':
            list_waves
        elif choice == '3':
            list_surfers
        elif choice == '4':
            list_surfboards
        elif choice == '5':
            find_beach_by_name
        elif choice == '20':
            exit_program
            break
        else:
            print("Invalid choice")
            
            

if __name__ == "__main__":
    main()