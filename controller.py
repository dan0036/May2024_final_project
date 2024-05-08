import animal
import db_queries
import model
import view
import text


db = list()
last_id: int


def start():
    connection_local = \
        (model.create_connection(
            "Localhost",
            "root",
            "Russia2024",
            "dan_1"
        ))
    connection = \
        (model.create_connection(
            "bkdarmqasjriytsv8kxg-mysql.services.clever-cloud.com",
            "uzatpacf58x8totx",
            "tqMtmmKocQlYXfzOyXmu",
            "bkdarmqasjriytsv8kxg"
        ))

    model.execute_query(connection, db_queries.create_table_animals)

    model.update_db()
    print(text.open_successful)

    while True:
        choice = view.main_menu()
        match choice:
            case '1':  # prints all animals arranged by date
                print(text.view_animal_by_date)
                for e in model.execute_read_query(connection, db_queries.select_all_animals_by_bitrhd):
                    print(e)
                # model.show_db()
            case '2':  # add animal
                type = input(text.input_new_animal_type)
                nick = input(text.input_new_animal_nick)
                birthd = input(text.input_new_animal_birthd)
                commands = input(text.input_new_animal_commands)
                model.execute_query(connection, db_queries.insert_animal(type, nick, birthd, commands))
                # model.add_animal(type, nick, birthd, commands)
                # model.update_db()
            case '3':  # find animal
                find = input(text.input_search_nick)
                try:
                    for e in model.execute_read_query(connection, db_queries.find_animal(find)):
                        print(e)
                except:
                    print(text.search_animal_error(find))
                # model.print_animal_from_class(model.detect_int_str_animal_search(find))
            case '4':  # edit animal
                try:
                    find = input(text.input_search_nick)
                    assert model.execute_read_query(connection, db_queries.find_animal(find)) !=[]
                    print(model.execute_read_query(connection, db_queries.find_animal(find)))
                    type = input(text.input_type_to_edit)
                    nick = input(text.input_nick_to_edit)
                    birthd = input(text.input_birthd_to_edit)
                    commands = input(text.input_commands_to_edit)

                    model.execute_query(connection, db_queries.edit_animal(find, type, nick, birthd, commands))
                except:
                    print(text.search_animal_error(find))
                # model.edit_animal(id_edit, type, message, db)
                # model.update_db()
            case '5':  # delete animal
                try:
                    find = input(text.input_search_nick)
                    assert model.execute_read_query(connection, db_queries.find_animal(find)) != []
                    print(model.execute_read_query(connection, db_queries.find_animal(find)))
                    model.execute_query(connection, db_queries.delete_animal(find))
                except:
                    print(text.search_animal_error(find))
                # id_edit = int(input(text.input_delete_id))
                # model.delete_animal(id_edit, db)
            case '6':
                break
