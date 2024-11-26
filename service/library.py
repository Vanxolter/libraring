import json
from service.book import Book
from utils.decorators import save_after_action, handle_exceptions
from utils.validators import validate_title, validate_author, validate_year


class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        books (list[Book]): Список всех книг в библиотеке.
        storage_file (str): Путь к файлу хранения данных.
        _next_id (int): Уникальный идентификатор для новой книги.

    Методы:
        __init__: Инициализирует библиотеку и загружает книги из файла.
        add_book: Добавляет книгу в библиотеку или увеличивает её количество, если книга уже существует.
        remove_book: Удаляет книгу из библиотеки по её идентификатору.
        find_book_by_id: Находит книгу по её идентификатору.
        find_books: Находит книги по заданным критериям (названию, автору, году).
        update_status: Изменяет статус книги (например, "выдана" или "в наличии").
        display_books: Выводит список всех книг в библиотеке.
        load_books: Загружает книги из указанного файла.
        save_books: Сохраняет текущий список книг в файл.
        _generate_id: Генерирует уникальный идентификатор для новой книги.
        _issue_book: Выдаёт книгу, уменьшая её количество.
        _return_book: Возвращает книгу, увеличивая её количество.
    """

    def __init__(self, storage_file: str = "data/library.json"):
        """
        Инициализирует объект класса Library и загружает книги из файла.

        Аргументы:
            storage_file (str): Путь к файлу хранения данных. По умолчанию "data/library.json".
        """
        self.books: list[Book] = []
        self.storage_file = storage_file
        self.load_books()
        self._next_id = self.books[-1].book_id + 1 if len(self.books) > 0 else 1

    @save_after_action
    def add_book(self, title: str, author: str, year: int, validated: int = 0) -> Book:
        """
        Добавляет книгу в библиотеку или увеличивает её количество, если книга уже существует.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.

        Возвращает:
            Book: Добавленная или обновлённая книга.
        """
        book_exists = self.find_books(title, author, year)
        if not book_exists:
            new_id: int = self._generate_id()
            book = Book(book_id=new_id, title=title, author=author, year=year)
            self.books.append(book)
        else:
            book = book_exists[0]
            self._return_book(book)
        return book

    @save_after_action
    def remove_book(self, book_id: int) -> bool:
        """
        Удаляет книгу из библиотеки по её идентификатору.

        Аргументы:
            book_id (int): Уникальный идентификатор книги.

        Возвращает:
            bool: True, если книга была удалена, иначе False.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False

    def find_book_by_id(self, book_id: int) -> Book | None:
        """
        Находит книгу по её идентификатору.

        Аргументы:
            book_id (int): Уникальный идентификатор книги.

        Возвращает:
            Book | None: Найденная книга или None, если книга не найдена.
        """
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_books(self, title: str | None = None, author: str | None = None, year: int | None = None) -> list[Book]:
        """
        Ищет книги по заданным критериям (названию, автору или году).

        Аргументы:
            title (str | None): Название книги (необязательно).
            author (str | None): Автор книги (необязательно).
            year (int | None): Год издания книги (необязательно).

        Возвращает:
            list[Book]: Список найденных книг.
        """

        def matches_criteria(book):
            return (
                    (not title or (title.lower() in book.title.lower() and len(title) == len(book.title))) and
                    (not author or (author.lower() in book.author.lower() and len(author) == len(book.author))) and
                    (not year or book.year == year)
            )

        return [book for book in self.books if matches_criteria(book)]

    @save_after_action
    def update_status(self, book_id: int, status: str) -> bool:
        """
        Изменяет статус книги ("выдана" или "в наличии").

        Аргументы:
            book_id (int): Уникальный идентификатор книги.
            status (str): Новый статус книги.

        Возвращает:
            bool: True, если статус был успешно обновлён, иначе False.
        """
        book = self.find_book_by_id(book_id)
        actions = {
            "выдана": lambda: book.count > 0 and self._issue_book(book),
            "в наличии": lambda: self._return_book(book),
        }
        return actions.get(status, lambda: False)()

    @staticmethod
    def _issue_book(book: Book) -> bool:
        """
        Выдаёт книгу, уменьшая её количество.

        Аргументы:
            book (Book): Книга для выдачи.

        Возвращает:
            bool: True, если книга была успешно выдана.
        """
        book.count -= 1
        if book.count == 0:
            book.status = "выдана"
        return True

    @staticmethod
    def _return_book(book: Book) -> bool:
        """
        Возвращает книгу, увеличивая её количество.

        Аргументы:
            book (Book): Книга для возврата.

        Возвращает:
            bool: True, если книга была успешно возвращена.
        """
        book.count += 1
        book.status = "в наличии"
        return True

    def display_books(self) -> bool:
        """
        Выводит список всех книг в библиотеке.
        """
        if not self.books:
            print("Библиотека пуста.")
            return False
        for book in self.books:
            print(book)
        return True

    @handle_exceptions
    def load_books(self) -> None:
        """
        Загружает книги из указанного файла.

        Исключения:
            FileNotFoundError: Если файл не существует.
            JSONDecodeError: Если файл содержит некорректные данные.
        """
        with open(self.storage_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.books = [Book.from_dict(book) for book in data]

    def save_books(self) -> None:
        """
        Сохраняет текущий список книг в файл.
        """
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def _generate_id(self) -> int:
        """
        Генерирует уникальный идентификатор для новой книги.

        Возвращает:
            int: Уникальный идентификатор.
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id
