import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Функция для загрузки данных из файла
def load_phonebook(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().split(',') for line in file]

# Функция для сохранения данных в файл
def save_phonebook(phonebook, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(','.join(entry) + '\n' for entry in phonebook)

# Функция для отображения записей
def display_phonebook(phonebook):
    return '\n'.join(f'Фамилия: {entry[0]}, Имя: {entry[1]}, Отчество: {entry[2]}, Телефон: {entry[3]}' for entry in phonebook)

# Функция для поиска записей по запросу
def search_phonebook(phonebook, query):
    return [entry for entry in phonebook if query in entry]

# Функция для добавления новой записи
def add_entry(phonebook, entry):
    phonebook.append(entry)

# Функция для обновления записи
def update_entry(phonebook, query, new_entry):
    for i, entry in enumerate(phonebook):
        if query in entry:
            phonebook[i] = new_entry
            break

# Функция для удаления записи
def delete_entry(phonebook, query):
    phonebook[:] = [entry for entry in phonebook if query not in entry]

# Функция для обработки событий интерфейса
def handle_event(event_type, phonebook, phonebook_file, entries, query_entry):
    if event_type == 'show':
        result = display_phonebook(phonebook)
        messagebox.showinfo("Phonebook Entries", result)
    elif event_type == 'add':
        new_entry = [entry.get() for entry in entries]
        add_entry(phonebook, new_entry)
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry added successfully")
    elif event_type == 'search':
        query = query_entry.get()
        results = search_phonebook(phonebook, query)
        result = display_phonebook(results)
        messagebox.showinfo("Search Results", result)
    elif event_type == 'update':
        query = query_entry.get()
        new_entry = [entry.get() for entry in entries]
        update_entry(phonebook, query, new_entry)
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry updated successfully")
    elif event_type == 'delete':
        query = query_entry.get()
        delete_entry(phonebook, query)
        save_phonebook(phonebook, phonebook_file)
        messagebox.showinfo("Info", "Entry deleted successfully")

# Главная функция программы
def main():
    phonebook_file = 'phonebook.txt'
    phonebook = load_phonebook(phonebook_file)

    root = tk.Tk()
    root.title("Phonebook")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10), padding=5)
    style.configure("TLabel", font=("Arial", 10))
    style.configure("TEntry", font=("Arial", 10))

    labels_text = ["Фамилия", "Имя", "Отчество", "Телефон", "Поиск"]
    entries = [ttk.Entry(root) for _ in range(4)]
    query_entry = ttk.Entry(root)

    for i, text in enumerate(labels_text[:4]):
        ttk.Label(root, text=text).grid(row=i, column=0, padx=10, pady=5)
        entries[i].grid(row=i, column=1, padx=10, pady=5)

    ttk.Label(root, text=labels_text[4]).grid(row=4, column=0, padx=10, pady=5)
    query_entry.grid(row=4, column=1, padx=10, pady=5)

    buttons = [
        ("Показать все", 'show'),
        ("Добавить", 'add'),
        ("Найти", 'search'),
        ("Изменить", 'update'),
        ("Удалить", 'delete')
    ]

    for i, (text, event_type) in enumerate(buttons):
        ttk.Button(root, text=text, command=lambda e=event_type: handle_event(e, phonebook, phonebook_file, entries, query_entry)).grid(row=5 + i // 2, column=i % 2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
