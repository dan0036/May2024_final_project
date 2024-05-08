import json

import animal
import controller
import text


def load_db(filename='db.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return ["База данных не найдена!\n"]


def load_last_id(db: list):
    return db[len(db) - 1].get("id")


def update_db():
    controller.db = load_db()
    controller.last_id = controller.db[0].get('last_id')


def save_db(db, filename='db.json'):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)


def init_id_animal_db(e: int):
    try:
        for i in controller.db:
            if i.get('id') == e:
                return animal.Animal(
                    i['id'],
                    i['type'],
                    i['nick'],
                    i['birthd'],
                    i['commands'])
        raise Exception('Err. No such id!')
    except Exception as err:
        pass # print(err)



def init_nick_animal_db(nick: str):
    for dict_animal in controller.db:
        if dict_animal.get('nick') == nick:
            return animal.Animal(dict_animal['id'],
                          dict_animal['type'],
                          dict_animal['nick'],
                          dict_animal['birthd'],
                          dict_animal['commands'])


def add_animal(an: animal):
    animal_db = {'id': an.id,
                 'type': an.type,
                 'nick': an.nick,
                 'birthd': an.birthd,
                 'commands': an.commands}
    controller.db.append(animal_db)
    save_db(controller.db)
    print('Animal save successful.')

def add_animal(type, nick, birthd, commands):

    animal_db = {'id': controller.last_id,
                 'type': type,
                 'nick': nick,
                 'birthd': birthd,
                 'commands': commands}
    controller.db.append(animal_db)
    controller.last_id += 1
    controller.db[0]['last_id'] = controller.last_id
    save_db(controller.db)
    print('Animal save successful.')



def show_db():
    sorted_db = sorted(controller.db, key=lambda x: x.get('birthd'))
    print('*** db start ***')
    for an in sorted_db:
        print_animal_from_dict(an)
    print('*** db end ***')

def print_animal_from_dict(an):
    print(f"id: {an.get('id')}\n"
          f"type: {an.get('type')}\n"
          f"nick: {an.get('nick')}\n"
          f"birthd: {an.get('birthd')}\n"
          f"commands: {an.get('commands')}")

def print_animal_from_class(a):
    try:
        print(f"id: {a.id}\n"
          f"type: {a.type}\n"
          f"nick: {a.nick}\n"
          f"birthd: {a.birthd}\n"
          f"commands: {a.commands}")
    except:
        print(text.search_result_none)


def detect_int_str_animal_search(income): # returnes class Animal object
    try:
        int(income)
        return init_id_animal_db(income)
    except:
        return init_nick_animal_db(income)

    # found_db = list()
    # for animal in db:
    #     if find in (animal.get('title') or animal.get('message')):
    #         found_db.append(animal)
    # if len(found_db) > 0:
    #     return found_db
    # else:
    #     none_result = list()
    #     none_result.append(text.search_animal_error(find))
    #     return none_result


def edit_animal(animal_id, title, message, db: list):
    for animal in db:
        if animal.get('id') == animal_id:
            print('**'+title+'**')
            if title != '':
                animal.update({'title': title})
            if message != '':
                animal.update({'message': message})
            animal.update({'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            save_db(db)
            print('animal edition successful.')
            return
    print(f"animal with id {animal_id} not found.")


def delete_animal(animal_id, db):
    for animal in db:
        if animal.get('id') == animal_id:
            db.remove(animal)
            save_db(db)
            print('animal deletion successful.')
            return
    print(f"animal with id {animal_id} not found.")
