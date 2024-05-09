import animal
import db_queries
import model
import view
import text

db = list()
last_id: int


def start():
    # connection = \
    #     (model.create_connection(
    #         "Localhost",
    #         "root",
    #         "Russia2024",
    #         "dan_1"
    #     ))

    connection = \
        (model.create_connection(
            "bkdarmqasjriytsv8kxg-mysql.services.clever-cloud.com",
            "uzatpacf58x8totx",
            "tqMtmmKocQlYXfzOyXmu",
            "bkdarmqasjriytsv8kxg"
        ))

    model.execute_query(connection, db_queries.create_table_animals)

    try:
        model.execute_query(connection, db_queries.insert_table_animals)
    except:
        pass

    model.execute_query(connection, db_queries.create_table_dogs)

    model.execute_query(connection, db_queries.create_table_cats)

    model.execute_query(connection, db_queries.create_table_hamsters)

    # model.update_db()
    print(text.open_successful)

    while True:
        choice = view.main_menu()
        match choice:
            case '1':  # prints all animals arranged by date
                print(text.view_animal_by_date)
                for e in model.execute_read_query(connection, db_queries.select_all_animals_by_birthd):
                    print(e)
                # model.show_db()
            case '2':  # add animal
                type = input(text.input_new_animal_type).lower()
                nick = input(text.input_new_animal_nick).upper()
                birthd = input(text.input_new_animal_birthd)
                commands = input(text.input_new_animal_commands).lower()
                try:
                    model.execute_query(connection, db_queries.insert_animal(type, nick, birthd, commands))
                except:
                    pass
                # model.add_animal(type, nick, birthd, commands)
                # model.update_db()
            case '3':  # find animal
                find = input(text.input_search_nick).upper()
                try:
                    assert model.execute_read_query(connection, db_queries.find_animal(find)) != []
                    for e in model.execute_read_query(connection, db_queries.find_animal(find)):
                        print(e)

                except:
                    print(text.search_animal_error(find))
                # model.print_animal_from_class(model.detect_int_str_animal_search(find))
            case '4':  # edit animal
                try:
                    find = input(text.input_search_nick).upper()
                    assert model.execute_read_query(connection, db_queries.find_animal(find)) != []
                    print(model.execute_read_query(connection, db_queries.find_animal(find)))
                    nick = input(text.input_nick_to_edit).upper()
                    birthd = input(text.input_birthd_to_edit)
                    commands = input(text.input_commands_to_edit).lower()
                    type = model.execute_read_query(connection, db_queries.find_type_by_nick(find))
                    if len(type) == 1 and len(type[0]) == 1:
                        model.execute_query(connection,
                                            db_queries.edit_animal(type[0][0], find, nick, birthd, commands))
                    else:
                        raise IOError
                except Exception as e:
                    print(e)
                    print(text.search_animal_error(find))
                # model.edit_animal(id_edit, type, message, db)
                # model.update_db()
            case '5':  # delete animal
                try:
                    find = input(text.input_search_nick).upper()
                    assert model.execute_read_query(connection, db_queries.find_animal(find)) != []
                    type = model.execute_read_query(connection, db_queries.find_type_by_nick(find))
                    assert len(type) == 1 and len(type[0]) == 1
                    print(model.execute_read_query(connection, db_queries.find_animal(find)))
                    assert input(text.confirm_delete_animal(type[0][0], find)).lower() == 'y'
                    model.execute_query(connection, db_queries.delete_animal(type[0][0], find))
                except:
                    print(text.search_animal_error(find))
            case '6':
                try:
                    find = input(text.input_search_nick).upper()
                    print(model.execute_read_query(connection, db_queries.find_animal_commands(find))[0][0])
                except:
                    print(text.search_animal_error(find))
            case '7':
                try:
                    type = input(text.input_search_type).lower()
                    print(model.execute_read_query(connection, db_queries.count_animals(type))[0][0])
                except:
                    print(text.search_animal_error(find))
            case '8':
                break
