import menu
import data_handler

def main():
    csv = None
    while True:
        menu.display_main_menu()
        menu_input = menu.get_menu_input()
        # last choice will always be exit so exit if it is
        if menu_input == len(menu.return_choices()):
            break
        # always save csv so it can be referenced
        else:
            csv = data_handler.route_menu_input(menu_input, csv)

    print("Exiting program...")


if __name__ == "__main__":
    main()