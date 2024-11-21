from utils.decorators import handle_exceptions
from service.library import Library
from settings.settings import APP_NAME
from utils.validators import validate_input, validate_title, validate_author, validate_year


class Runner:
    """Класс для запуска приложения управления библиотекой."""

    def __init__(self):
        self.library = Library()

    def __display_menu(self) -> None:
        """Выводит меню команд."""
        print("Выберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

    def __display_name(self):
        """Выводит имя приложения 1 раз"""
        names = APP_NAME
        for name in names:
            print(name)

    def run(self):
        """Запускает основной цикл приложения."""
        self.__display_name()
        while True:
            self.__display_menu()
            choice = input("Введите номер команды: ").strip()
            try:
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.remove_book()
                elif choice == "3":
                    self.find_books()
                elif choice == "4":
                    self.display_books()
                elif choice == "5":
                    self.update_status()
                elif choice == "6":
                    print("Выход из приложения. До свидания!")
                    break
                else:
                    print("Неверный выбор. Попробуйте снова.")
            except Exception as e:
                print(f"Ошибка: {e}")

    def add_book(self):
        """Добавляет новую книгу."""
        title = validate_input("Введите название книги: ", validate_title)
        author = validate_input("Введите автора книги: ", validate_author)
        year = validate_input("Введите год издания: ", validate_year)

        book = self.library.add_book(title=title, author=author, year=year)
        print(f"Книга добавлена: {book.title} (ID: {book.book_id})")

    def remove_book(self):
        """Удаляет книгу по ID."""
        book_id = input("Введите ID книги, которую нужно удалить: ").strip()
        if not book_id.isdigit():
            raise ValueError("ID должен быть числом.")
        success = self.library.remove_book(int(book_id))
        if success:
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_books(self):
        """Ищет книги по различным критериям."""
        criteria = {
            "1": ("название книги", "title"),
            "2": ("автора книги", "author"),
            "3": ("год издания", "year"),
        }

        print("\nВыберите критерий поиска:")
        for key, (label, _) in criteria.items():
            print(f"{key}. По {label}")

        choice = input("Введите номер критерия: ").strip()
        if choice not in criteria:
            print("Неверный выбор. Возврат в главное меню.")
            return

        label, field = criteria[choice]
        value = input(f"Введите {label}: ").strip()
        if field == "year":
            value = validate_year(value)

        books = self.library.find_books(**{field: value})
        if books:
            print("\nНайденные книги:")
            for book in books:
                print(
                    f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, "
                    f"Год: {book.year}, Статус: {book.status}"
                )
        else:
            print("Книги не найдены.")

    def display_books(self):
        """Выводит список всех книг."""
        print("\nСписок всех книг:")
        self.library.display_books()

    def update_status(self):
        """Обновляет статус книги."""
        book_id = input("Введите ID книги: ").strip()
        if not book_id.isdigit():
            raise ValueError("ID должен быть числом.")

        status = input("Введите новый статус (в наличии/выдана): ").strip()
        if status not in ["в наличии", "выдана"]:
            raise ValueError("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
        success = self.library.update_status(int(book_id), status)
        if success:
            print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def exit(self):
        """Завершение выполнения приложения"""
        print("Выход из приложения. До свидания!")
        exit()
