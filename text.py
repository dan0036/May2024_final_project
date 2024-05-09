main_menu = ['Главное меню картотеки',
             'Показать всех животных картотеки (сортировка по дате рождения)',
             'Добавить животное в картотеку',
             'Найти животное по кличке',
             'Изменить данные о животном',
             'Удалить животное из картотеки',
             'Показать команды, выполняемые животным'
             'Выход']

input_main_menu = 'Выберите пункт меню: '
input_main_menu_error = f'Выберите пункт меню, число от 1 до {len(main_menu)-1}'

open_successful = 'Картотека успешно открыта.'
save_successful = 'Картотека успешно сохранена.'

empty_animal_book_error = 'Картотека пуста или не открыта'

view_animal_by_date = 'Вывод всех зверей питомника отсортированных по дате рождения: '

input_new_animal_type = 'Введите тип животного: '
input_new_animal_nick = 'Введите кличку животного: '
input_new_animal_birthd = 'Введите дату рождения формата: ГГГГ-ММ-ДД: '
input_new_animal_commands = 'Введите выполяемые команды через запятую: '

input_search_nick = 'Введите кличку для поиска: '

input_nick_to_edit = 'Введите кличку животного или Enter (без изменений): '
input_birthd_to_edit = 'Введите дату рождения животного или Enter (без изменений): '
input_commands_to_edit = 'Введите комманды для животного или Enter (без изменений): '

search_result_none = 'Запись с искомым запросом не найдена.'

type_animal_not_exists = 'Введен несуществующий тип животного.'

input_nick_to_edit = 'Введите новую кличку животного или Enter (без изменений): '

confirm_delete_animal = lambda x, y: f'Вы действительно хотите удалить животное {x} по кличке {y}? (y/n)'

good_bye = 'До свидания.'

def animal_successful_result(name: str, mode: int) -> str:
    return f'запись {name} успешно {animal_actions[mode]}.'

def search_animal_error(word: str) -> str:
    return f'записи, содержащие {word}, не найдены.'