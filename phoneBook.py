from person import Person


class PhoneBook:
    """Класс отвечающий за работу с записями. Работает со списком"""

    def __init__(self):
        self.phonebook = []

    def add_person(self, person: Person) -> None:
        """Метод добавляющий в список запись. В дальнейшем можно добавить фильтр
        добавления"""
        self.phonebook.append(person)

    def display_phonebook(self) -> None | list[Person]:
        """Метод выводящий весь список записей и возвращающий его.
        Можно добавить выборку для использования в консоли или простого возврата
        добавив простой параметр"""
        for person in self.phonebook:
            print(
                f'Имя: {person.name}\n'
                f'Фамилия: {person.second_name}\n'
                f'Отчество: {person.third_name}\n'
                f'Организация: {person.organization}\n'
                f'Рабочий телефон: {person.work_phone}\n'
                f'Личный номер: {person.personal_number}\n')
        return self.phonebook

    def search_by_second_name(self, second_name: str) -> None | list[Person]:
        """Поиск записей по фамилии. Выводи в консоль и возвращает список
        найденных записей. Так же как и прошлый метод Можно добавить выборку
        возврата, вывода или двойного действия.
        Поиск совершается путем перебора и сравнения значений"""
        search_result = []
        for person in self.phonebook:
            if person.second_name == second_name:
                search_result.append(person)
                print(
                    f'Имя: {person.name}\n'
                    f'Фамилия: {person.second_name}\n'
                    f'Отчество: {person.third_name}\n'
                    f'Организация: {person.organization}\n'
                    f'Рабочий телефон: {person.work_phone}\n'
                    f'Личный номер: {person.personal_number}\n')
        return search_result

    def search_by_organization(self, organization: str) -> None | list[Person]:
        """Аналогичен предыдущему методу. Поиск по организации"""
        search_result = []
        for person in self.phonebook:
            if person.organization == organization:
                search_result.append(person)
                print(
                    f'Имя: {person.name}\n'
                    f'Фамилия: {person.second_name}\n'
                    f'Отчество: {person.third_name}\n'
                    f'Организация: {person.organization}\n'
                    f'Рабочий телефон: {person.work_phone}\n'
                    f'Личный номер: {person.personal_number}\n')
        return search_result

    def edit_person_second_name(self, second_name: str) -> None:
        """Редактирование записи. Поиск нужной записи по фамилии.
        В случае нескольких совпадений, предлагает выбор, какую
        из записей редактировать"""
        persons = [person for person in self.phonebook if person.second_name == second_name]
        if not persons:
            print("Нет людей с такой фамилией.")
            return

        for i, person in enumerate(persons, start=1):
            print(
                f"{i}. Имя: {person.name}, Фамилия: {person.second_name}, Отчество: {person.third_name}, Организация: {person.organization}, Рабочий телефон: {person.work_phone}, Личный номер: {person.personal_number}")

        person_number = int(input("Введите номер записи, которую вы хотите отредактировать: ")) - 1
        if person_number not in range(len(persons)):
            print("Неверный номер.")
            return

        person_to_edit = persons[person_number]
        person_to_edit.second_name = input("Введите новую фамилию: ")
        person_to_edit.name = input("Введите новое имя: ")
        person_to_edit.third_name = input("Введите новое отчество: ")
        person_to_edit.organization = input("Введите новую организацию: ")
        person_to_edit.work_phone = input("Введите новый рабочий телефон: ")
        person_to_edit.personal_number = input("Введите новый личный номер: ")

        print("Запись успешно отредактирована.")
