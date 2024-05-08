import text

def main_menu():
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'{i}. {text.main_menu[i]}')
    while True:
        choice = input(text.input_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return choice
        else:
            print(text.input_main_menu_error)

def choice_switch():
    answer = input('Type: "y" or press Enter').lower()
    if answer == 'y':
        return True
    else:
        return False