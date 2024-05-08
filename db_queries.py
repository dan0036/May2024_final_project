import text

create_table_animals = """
        CREATE TABLE IF NOT EXISTS animals (
          id SERIAL PRIMARY KEY,
          type VARCHAR(12),
          nick VARCHAR(26) NOT NULL,
          birthd DATE,
          commands VARCHAR(80)
          );
        """
select_all_animals_by_bitrhd = """
    SELECT * FROM animals
    ORDER BY birthd;
"""
def insert_animal(type, nick, birthd, commands):
    return f"""
    INSERT INTO animals
    (type, nick, birthd, commands)
    VALUES
    ('{type}', '{nick}', '{birthd}', '{commands}');"""

def find_animal(find):
    return f"""
    SELECT * FROM animals
    WHERE nick='{find}'; """

def edit_animal(find, type, nick, birthd, commands):
    result = f""" 
    UPDATE animals
    SET
    {f" type ='{type}'" if type!='' else ''}
    {", " if type!='' and nick!='' else ''}
    {f" nick ='{nick}'" if nick!='' else ''}
    {", " if birthd!='' and nick!='' else ''}
    {f" birthd = '{birthd}'" if birthd!='' else ''}
    {", " if birthd!='' and commands!='' else ''}
    {f" commands ='{commands}'" if commands!='' else ''}
    WHERE nick = '{find}';
    """
    return result

def delete_animal(find):
    return f"""
        DELETE FROM animals
        WHERE nick='{find}'; """