import json
from service.book import Book
from utils.decorators import save_after_action, handle_exceptions


class Library:
    """Класс, представляющий библиотеку."""

    def __init__(self, storage_file: str = "data/library.json"):
        self.books: list[Book] = []
        self.storage_file = storage_file
        self.load_books()

    @save_after_action
    def add_book(self, title: str, author: str, year: int) -> Book:
        """Добавляет книгу в библиотеку."""
        new_id = self._generate_id()
        book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books.append(book)
        return book

    @save_after_action
    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу из библиотеки по id."""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            return True
        return False

    def find_book_by_id(self, book_id: int) -> Book | None:
        """Ищет книгу по id."""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_books(self, title: str | None = None, author: str | None = None, year: int | None = None) -> list[Book]:
        """Ищет книги по title, author или year."""
        result = self.books
        if title:
            result = [book for book in result if title.lower() in book.title.lower()]
        if author:
            result = [book for book in result if author.lower() in book.author.lower()]
        if year:
            result = [book for book in result if book.year == year]
        return result

    @save_after_action
    def update_status(self, book_id: int, status: str) -> bool:
        """Обновляет статус книги."""
        if status not in ["в наличии", "выдана"]:
            raise ValueError("Некорректный статус. Допустимые значения: 'в наличии', 'выдана'.")
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            return True
        return False

    def display_books(self) -> None:
        """Выводит список всех книг."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book.book_id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    @handle_exceptions
    def load_books(self) -> None:
        """Загружает книги из файла."""

        with open(self.storage_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.books = [Book.from_dict(book) for book in data]

    def save_books(self) -> None:
        """Сохраняет книги в файл."""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def _generate_id(self) -> int:
        """Генерирует уникальный id для новой книги."""
        if not self.books:
            return 1
        return max(book.book_id for book in self.books) + 1
