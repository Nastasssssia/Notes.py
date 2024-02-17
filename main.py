import json
import os
from datetime import datetime

# Имя файла, в котором будут храниться заметки
NOTES_FILE = "notes.json"


# Функция для загрузки заметок из файла
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)


# Функция для добавления новой заметки
def add_note(title, msg):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": note_id,
        "title": title,
        "msg": msg,
        "timestamp": timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена.")


# Функция для вывода списка заметок
def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")


# Функция для просмотра отдельной заметки
def view_note(note_id):
    notes = load_notes()
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        print(f"{note['title']} ({note['timestamp']})\n{note['msg']}")
    else:
        print("Заметка не найдена.")


# Функция для редактирования существующей заметки
def edit_note(note_id, title, msg):
    notes = load_notes()
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        note["title"] = title
        note["msg"] = msg
        note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")


# Функция для удаления заметки
def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")


# Функция для фильтрации заметок по дате
def filter_notes_by_date(date):
    notes = load_notes()
    filtered_notes = [note for note in notes if note["timestamp"].startswith(date)]
    if not filtered_notes:
        print("Заметок на указанную дату не найдено.")
    else:
        for note in filtered_notes:
            print(f"{note['id']}. {note['title']} ({note['timestamp']})")


# Основная функция для взаимодействия с пользователем
def main():
    while True:
        print("\nВыберите команду:")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Просмотреть заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Фильтр по дате")
        print("0. Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            msg = input("Введите тело заметки: ")
            add_note(title, msg)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите номер заметки: "))
            view_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите номер заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            msg = input("Введите новое тело заметки: ")
            edit_note(note_id, title, msg)
        elif choice == "5":
            note_id = int(input("Введите номер заметки для удаления: "))
            delete_note(note_id)
        elif choice == "6":
            date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
            filter_notes_by_date(date)
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующую команду.")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
