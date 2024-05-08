import model
import view
import text

db = list()
last_id: int


def start():
    model.update_db()
    print(text.open_successful)

    while True:
        choice = view.main_menu()
        match choice:
            case '1':  # prints all animals arranged by date
                print(text.view_animal_by_date)
                model.show_db()
            case '2':  # add animal
                type = input(text.input_new_animal_type)
                nick = input(text.input_new_animal_nick)
                birthd = input(text.input_new_animal_birthd)
                commands = input(text.input_new_animal_commands)
                model.add_animal(type, nick, birthd, commands)
                model.update_db()
            case '3':  # find animal
                find = input(text.input_search_word)
                model.print_animal_from_class(model.detect_int_str_animal_search(find))
            case '4':  # edit animal
                id_edit = int(input(text.input_edit_id))
                type = input(text.input_edit_animal_title)
                message = input(text.input_new_animal_nick)
                model.edit_animal(id_edit, type, message, db)
                model.update_db()
            case '5':  # delete animal
                id_edit = int(input(text.input_delete_id))
                model.delete_animal(id_edit, db)
            case '6':
                break
