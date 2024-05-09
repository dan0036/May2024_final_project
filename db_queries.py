import model
import text

create_table_animals = """
        CREATE TABLE IF NOT EXISTS animals (
          id SERIAL PRIMARY KEY,
          type VARCHAR(12) UNIQUE
          );
          """

insert_table_animals = """    
        INSERT INTO animals (type)
        VALUES ('dog'), ('cat'), ('hamster');
        """
check_animals_ids = """
        SELECT id FROM animals;
        """

create_table_dogs = """
        CREATE TABLE IF NOT EXISTS dogs (
          id INT UNSIGNED NOT NULL UNIQUE PRIMARY KEY auto_increment,
          type VARCHAR(12) DEFAULT 'dog',
          nick VARCHAR(26) NOT NULL UNIQUE,
          birthd DATE,
          commands VARCHAR(80),
          id_animal INT UNSIGNED NOT NULL UNIQUE DEFAULT 1, 
          FOREIGN KEY (id_animal) REFERENCES animals(id)
          );
        """

create_table_cats = """
        CREATE TABLE IF NOT EXISTS cats (
          id INT UNSIGNED NOT NULL UNIQUE PRIMARY KEY auto_increment,
          type VARCHAR(12) DEFAULT 'cat',
          nick VARCHAR(26) NOT NULL UNIQUE,
          birthd DATE,
          commands VARCHAR(80),
          id_animal INT UNSIGNED NOT NULL UNIQUE DEFAULT 2, 
          FOREIGN KEY (id_animal) REFERENCES animals(id)
          );
        """

create_table_hamsters = """
        CREATE TABLE IF NOT EXISTS hamsters (
          id INT UNSIGNED NOT NULL UNIQUE PRIMARY KEY auto_increment,
          type VARCHAR(12) DEFAULT 'hamster',
          nick VARCHAR(26) NOT NULL UNIQUE,
          birthd DATE,
          commands VARCHAR(80),
          id_animal INT UNSIGNED NOT NULL UNIQUE DEFAULT 3, 
          FOREIGN KEY (id_animal) REFERENCES animals(id)
          );
        """

select_all_animals_by_birthd = """
    SELECT * FROM dogs
    UNION
    SELECT * FROM cats
    UNION
    SELECT * FROM hamsters
    ORDER BY birthd;
"""

count_animals = lambda x: \
    f"""
    SELECT COUNT(*) FROM {x}s;
    """


def insert_animal(type, nick, birthd, commands):
    if model.check_type_animal(type):
        return f"""
        INSERT INTO {type}s
        (nick, birthd, commands)
        VALUES
        ('{nick}', '{birthd}', '{commands}');"""
    else:
        print(text.type_animal_not_exists)


def find_animal(find):
    return f"""
    SELECT * FROM dogs
    WHERE nick ='{find}'
    UNION
    SELECT * FROM cats
    WHERE nick ='{find}'
    UNION
    SELECT * FROM hamsters
    WHERE nick ='{find}'; """


def find_animal_commands(find):
    return f"""
    SELECT commands FROM dogs
    WHERE nick ='{find}'
    UNION
    SELECT commands FROM cats
    WHERE nick ='{find}'
    UNION
    SELECT commands FROM hamsters
    WHERE nick ='{find}'; """


def find_type_by_nick(find):
    return f"""
        SELECT type FROM dogs
        WHERE nick ='{find}'
        UNION
        SELECT type FROM cats
        WHERE nick ='{find}'
        UNION
        SELECT type FROM hamsters
        WHERE nick='{find}'; """


def edit_animal(type, find, nick, birthd, commands):
    result = f""" 
    UPDATE {type}s
    SET
    {f" nick ='{nick}'" if nick != '' else ''}
    {", " if birthd != '' and nick != '' else ''}
    {f" birthd = '{birthd}'" if birthd != '' else ''}
    {", " if birthd != '' and commands != '' else ''}
    {f" commands ='{commands}'" if commands != '' else ''}
    WHERE nick = '{find}';
    """
    return result


def delete_animal(type, find):
    return f"""
        DELETE FROM {type}s
        WHERE nick='{find}'; """
