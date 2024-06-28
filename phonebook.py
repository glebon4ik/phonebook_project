import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Функция для загрузки телефонного справочника из файла
def load_phonebook(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        phonebook = [line.strip().split(',') for line in file]
    return phonebook

# Функция для сохранения телефонного справочника в файл
def save_phonebook(phonebook, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(','.join(entry) + '\n')

# Функция для отображения телефонного справочника
def display_phonebook(phonebook):
    result = ""
    for entry in phonebook:
        result += f'Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}\n'
    return result

# Функция для поиска записей в телефонном справочнике
def search_phonebook(phonebook, query):
    results = [entry for entry in phonebook if query in entry]
    return results

# Функция для добавления новой записи в телефонный справочник
def add_entry(phonebook, surname, name, patronymic, phone):
    phonebook.append([surname, name, patronymic, phone])

# Функция для обновления существующей записи в телефонном справочнике
def update_entry(phonebook, query, new_entry):
    for i, entry in enumerate(phonebook):
        if query in entry:
            phonebook[i] = new_entry
            break

# Функция для удаления записи из телефонного справочника
def delete_entry(phonebook, query):
    phonebook[:] = [entry for entry in phonebook if query not in entry]

# Главная функция программы
def main():
    phonebook_file = 'phonebook.txt'
    phonebook = load_phonebook(phonebook_file)

    # Следующий код был создан с использованием ChatGPT для создания графического интерфейса с помощью tkinter и ttk
    def on_show():
        result = display_phonebook(phonebook)
        messagebox.showinfo("Phonebook Entries", result)

    def on_add():
        add_entry(phonebook, entry_surname.get(), entry_name.get(), entry_patronymic.get(), entry_phone.get())
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry added successfully")

    def on_search():
        results = search_phonebook(phonebook, entry_search.get())
        result = display_phonebook(results)
        messagebox.showinfo("Search Results", result)

    def on_update():
        query = entry_search.get()
        update_entry(phonebook, query, [entry_surname.get(), entry_name.get(), entry_patronymic.get(), entry_phone.get()])
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry updated successfully")

    def on_delete():
        query = entry_search.get()
        delete_entry(phonebook, query)
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry deleted successfully")

    # Создание главного окна приложения
    root = tk.Tk()
    root.title("Phonebook")
    root.geometry("400x300")

    # Настройка стиля интерфейса
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10), padding=5)
    style.configure("TLabel", font=("Arial", 10))
    style.configure("TEntry", font=("Arial", 10))

    # Создание меток и полей ввода
    ttk.Label(root, text="Фамилия").grid(row=0, column=0, padx=10, pady=5)
    ttk.Label(root, text="Имя").grid(row=1, column=0, padx=10, pady=5)
    ttk.Label(root, text="Отчество").grid(row=2, column=0, padx=10, pady=5)
    ttk.Label(root, text="Телефон").grid(row=3, column=0, padx=10, pady=5)
    ttk.Label(root, text="Поиск").grid(row=4, column=0, padx=10, pady=5)

    entry_surname = ttk.Entry(root)
    entry_name = ttk.Entry(root)
    entry_patronymic = ttk.Entry(root)
    entry_phone = ttk.Entry(root)
    entry_search = ttk.Entry(root)

    entry_surname.grid(row=0, column=1, padx=10, pady=5)
    entry_name.grid(row=1, column=1, padx=10, pady=5)
    entry_patronymic.grid(row=2, column=1, padx=10, pady=5)
    entry_phone.grid(row=3, column=1, padx=10, pady=5)
    entry_search.grid(row=4, column=1, padx=10, pady=5)

    # Создание кнопок для управления телефонным справочником
    ttk.Button(root, text='Показать все', command=on_show).grid(row=5, column=0, padx=10, pady=5)
    ttk.Button(root, text='Добавить', command=on_add).grid(row=5, column=1, padx=10, pady=5)
    ttk.Button(root, text='Найти', command=on_search).grid(row=6, column=0, padx=10, pady=5)
    ttk.Button(root, text='Изменить', command=on_update).grid(row=6, column=1, padx=10, pady=5)
    ttk.Button(root, text='Удалить', command=on_delete).grid(row=7, column=0, padx=10, pady=5)

    # Запуск главного цикла приложения
    root.mainloop()

if __name__ == "__main__":
    main()
