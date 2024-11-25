from service.library import Library
from settings.settings import APP_NAME, STATUSES
from utils.decorators import handle_exceptions
from utils.validators import validate_input, validate_title, validate_author, validate_year, validate_id


class Runner:
    """
    Класс для запуска приложения управления библиотекой.

    Методы:
        __init__: Инициализирует объект класса.
        _display_menu: Выводит меню команд для взасновной цикл приложения.
        add_book_interactive: Интерактивное добавление новой книги в библиотеку.
        remove_book_interactive: Удаляет книгу по идентификатору.
        find_books_intимодействия с пользователем.
        _display_name: Выводит название приложения при запуске.
        run: Запускает оeractive: Осуществляет поиск книг по заданным критериям.
        display_books_interactive: Отображает все книги, доступные в библиотеке.
        update_status_interactive: Изменяет статус книги.
        exit_interactive: Завершает выполнение приложения.
    """

    def __init__(self):
        """Инициализирует объект класса Runner и создает экземпляр библиотеки."""
        self.library = Library()

    @staticmethod
    def _display_menu() -> None:
        """
        Выводит меню команд для взаимодействия с пользователем.
        """
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

    @staticmethod
    def _display_name() -> None:
        """
        Выводит название приложения один раз при запуске.
        """
        names = APP_NAME
        for name in names:
            print(name)

    @handle_exceptions
    def run(self) -> None:
        """
        Запускает основной цикл приложения, позволяя пользователю выбирать команды из меню.
        """
        self._display_name()
        while True:
            self._display_menu()
            choice = input("Введите номер команды: ").strip()
            if choice == "1":
                self.add_book_interactive()
            elif choice == "2":
                self.remove_book_interactive()
            elif choice == "3":
                self.find_books_interactive()
            elif choice == "4":
                self.display_books_interactive()
            elif choice == "5":
                self.update_status_interactive()
            elif choice == "6":
                self.exit_interactive()
            else:
                print("Неверный выбор. Попробуйте снова.")

    def add_book_interactive(self) -> None:
        """
        Добавляет новую книгу в библиотеку с интерактивным вводом данных.
        """
        title = validate_input("Введите название книги: ", validate_title)
        author = validate_input("Введите автора книги: ", validate_author)
        year = validate_input("Введите год издания: ", validate_year)

        book = self.library.add_book(title=title, author=author, year=year)
        print(f"Книга добавлена: {book.title} (ID: {book.book_id})")

    def remove_book_interactive(self) -> None:
        """
        Удаляет книгу из библиотеки по идентификатору.
        """
        book_id = validate_input("Введите ID книги, которую нужно удалить: ", validate_id)
        success = self.library.remove_book(book_id)

        if success:
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_books_interactive(self) -> None:
        """
        Интерактивный поиск книг по названию, автору или году издания.
        """
        criteria = {
            "1": ("названию книги", "title"),
            "2": ("автору книги", "author"),
            "3": ("году издания", "year"),
        }

        print("\nВыберите критерии поиска (можно несколько через пробел):")
        for key, (label, _) in criteria.items():
            print(f"{key}. По {label}")

        choices = input("Введите номера критериев: ").strip().split()
        selected = {criteria[choice.strip()][1]: input(f"Введите {criteria[choice.strip()][0]}: ").strip()
                    for choice in choices if choice.strip() in criteria}

        if "title" in selected:
            selected["title"] = validate_title(selected["title"])
        if "author" in selected:
            selected["author"] = validate_author(selected["author"])
        if "year" in selected:
            selected["year"] = validate_year(selected["year"])

        books = self.library.find_books(
            title=selected.get("title"),
            author=selected.get("author"),
            year=selected.get("year"),
        )

        if books:
            print("\nНайденные книги:")
            for book in books:
                print(
                    f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, "
                    f"Год: {book.year}, Статус: {book.status}"
                )
        else:
            print("Книги не найдены.")

    def display_books_interactive(self) -> None:
        """
        Отображает список всех книг в библиотеке.
        """
        print("\nСписок всех книг:")
        self.library.display_books()

    def update_status_interactive(self) -> None:
        """
        Изменяет статус книги по идентификатору.
        """
        book_id = validate_input("Введите ID книги: ", validate_id)
        book = self.library.find_book_by_id(book_id)

        if not book:
            print(f"Книга с ID {book_id} не найдена.")
            return

        available_statuses = STATUSES - {book.status}  # Исключает текущий статус из доступных
        status = input(f"Введите новый статус из списка {available_statuses}: ").strip().lower()

        if status not in available_statuses:
            print(f"Некорректный статус. Допустимые значения: {available_statuses}.")
            return

        success = self.library.update_status(book_id, status)

        if success:
            print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
        else:
            print(f"Ошибка обновления статуса книги с ID {book_id}.")

    @staticmethod
    def exit_interactive() -> None:
        """
        Завершает выполнение приложения.
        """
        print("Выход из приложения. До свидания!")
        exit()
