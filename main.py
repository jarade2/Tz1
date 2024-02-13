from person import Person
from phoneBook import PhoneBook
from fileController import FileController


def main():
    book = PhoneBook()
    book.phonebook = FileController.load_from_file()

    while True:
        print("""\nВозможные действия.
1. Отобразить весь список
2. Добавить запись
3. Редактировать запись
4. Поиск записи
5. Выход\n""")
        user_choice = input("Выберите действие: ")

        if user_choice == "1":
            book.display_phonebook()
        elif user_choice == "2":
            book.add_person(Person(
                input("Фамилия: "),
                input("Имя: "),
                input("Отчество: "),
                input("Организация: "),
                input("Рабочий номер: "),
                input("Личный номер: ")
            ))
        elif user_choice == "3":
            book.edit_person_second_name(input("Введите фамилию изменяемой записи: "))
        elif user_choice == "4":
            user_choice = input("""По какому признаку искать?
1. Фамилия
2. Организация
Выбор: """)
            if user_choice == "1":
                book.search_by_second_name(input("Введите фамилию: "))
            elif user_choice == "2":
                book.search_by_organization(input("Введите название организации: "))
        elif user_choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

        FileController.save_to_file(book)


if __name__ == "__main__":
    main()
