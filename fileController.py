import json

from phoneBook import PhoneBook
from person import Person


class FileController:
    @staticmethod
    def save_to_file(phonebook: PhoneBook, filename: str = "test.json") -> None:
        """Сохранение объектов Person в объекты json
        Первый параметр - объект PhoneBook обязателен, представляет телефонную книгу.
        Хранит все записи в процессе работы программы.
        Второй параметр имя файлй для сохранения. Есть значение по умолчанию"""
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump([person.__dict__ for person in phonebook.phonebook], f)

    @staticmethod
    def load_from_file(filename: str = "test.json") -> list[Person]:
        """Метод возвращает список объектов Person, считанных из файла.
        Один необязательный параметр - имя файла с которого нужно считать
        объекты. В дальнейшем можно добавить выборку из какого файла считывать
        записи"""
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                return [Person(**person) for person in data]

        except (FileNotFoundError, json.JSONDecodeError):
            return []
