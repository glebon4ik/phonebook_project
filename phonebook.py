import os

def load_phonebook(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        phonebook = [line.strip().split(',') for line in file]
    return phonebook

def save_phonebook(phonebook, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(','.join(entry) + '\n')

def display_phonebook(phonebook):
    for entry in phonebook:
        print(f'Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}')

def search_phonebook(phonebook, query):
    results = [entry for entry in phonebook if query in entry]
    return results

def add_entry(phonebook, surname, name, patronymic, phone):
    phonebook.append([surname, name, patronymic, phone])

def update_entry(phonebook, query, new_entry):
    for i, entry in enumerate(phonebook):
        if query in entry:
            phonebook[i] = new_entry
            break

def delete_entry(phonebook, query):
    phonebook[:] = [entry for entry in phonebook if query not in entry]

def copy_entry(source_file, dest_file, line_number):
    phonebook = load_phonebook(source_file)
    if 0 < line_number <= len(phonebook):
        entry = phonebook[line_number - 1]
        dest_phonebook = load_phonebook(dest_file)
        dest_phonebook.append(entry)
        save_phonebook(dest_phonebook, dest_file)

def main():
    phonebook_file = 'phonebook.txt'
    phonebook = load_phonebook(phonebook_file)

    while True:
        print("Выберите действие: 1 - Показать все записи, 2 - Добавить запись, 3 - Найти запись, 4 - Изменить запись, 5 - Удалить запись, 6 - Копировать запись, 0 - Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            display_phonebook(phonebook)
        elif choice == '2':
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone = input("Введите номер телефона: ")
            add_entry(phonebook, surname, name, patronymic, phone)
            save_phonebook(phonebook, phonebook_file)
        elif choice == '3':
            query = input("Введите данные для поиска (имя, фамилию или телефон): ")
            results = search_phonebook(phonebook, query)
            display_phonebook(results)
        elif choice == '4':
            query = input("Введите данные для поиска записи для изменения: ")
            surname = input("Введите новую фамилию: ")
            name = input("Введите новое имя: ")
            patronymic = input("Введите новое отчество: ")
            phone = input("Введите новый номер телефона: ")
            update_entry(phonebook, query, [surname, name, patronymic, phone])
            save_phonebook(phonebook, phonebook_file)
        elif choice == '5':
            query = input("Введите данные для поиска записи для удаления: ")
            delete_entry(phonebook, query)
            save_phonebook(phonebook, phonebook_file)
        elif choice == '6':
            source_file = input("Введите имя файла источника: ")
            dest_file = input("Введите имя файла назначения: ")
            line_number = int(input("Введите номер строки для копирования: "))
            copy_entry(source_file, dest_file, line_number)
        elif choice == '0':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
