main_menu = ['Главное меню картотеки',
             'Показать всех животных картотеки (сортировка по дате рождения)',
             'Добавить животное в картотеку',
             'Найти животное по типу',
             'Изменить данные о животном',
             'Удалить животное из картотеки',
             'Выход']

input_main_menu = 'Выберите пункт меню: '
input_main_menu_error = f'Выберите пункт меню, число от 1 до {len(main_menu)-1}'



open_successful = 'Картотека успешно открыта.'
save_successful = 'Картотека успешно сохранена.'

empty_animal_book_error = 'Картотека пуста или не открыта'

view_animal_by_date = 'Вывод всех зверей питомника отсортированных по дате рождения: '
ask_input_date = 'Введите дату в формате: yyyy-mm-dd:'

input_new_animal_type = 'Введите тип животного: '
input_new_animal_nick = 'Введите кличку животного: '
input_new_animal_birthd = 'Введите дату рождения формата: ГГГГ-ММ-ДД: '
input_new_animal_commands = 'Введите выполяемые команды через запятую: '

input_search_word = 'Введите слово для поиска: '

input_edit_animal_title = 'Введите заголовок или Enter (без изменений): '
input_edit_animal_msg = 'Введите текст записи или Enter (без изменений): '

search_result_none = 'Запись с искомым запросом не найдена.'

input_edit_word = 'Введите ключевое слово для поиска записи, подлежащей изменению: '
input_delete_word = 'Введите ключевое слово для поиска записи, подлежащей удалению: '

input_delete_id = 'Введите ID записи, подлежащей удалению: '
input_edit_id = 'Введите ID записи, подлежащей изменению: '

animal_actions = ['сохранена', 'изменена', 'удалена']

confirm_delete_animal = lambda x: f'Вы действительно хотите удалить запись {x}? (y/n)'

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n) '

good_bye = 'До свидания.'

def animal_successful_result(name: str, mode: int) -> str:
    return f'запись {name} успешно {animal_actions[mode]}.'

def search_animal_error(word: str) -> str:
    return f'записи, содержащие {word}, не найдены.'