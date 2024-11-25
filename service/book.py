class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        book_id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год выпуска книги.
        status (str): Статус книги (по умолчанию "в наличии").
        count (int): Количество экземпляров книги (по умолчанию 1).
    """

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии", count: int = 1):
        """
        Инициализирует объект книги.

        Аргументы:
            book_id (int): Уникальный идентификатор книги.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год выпуска книги.
            status (str, optional): Статус книги (по умолчанию "в наличии").
            count (int, optional): Количество экземпляров книги (по умолчанию 1).
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.count = count

    def __str__(self):
        """
        Возвращает строковое представление книги.

        Возвращает:
            str: Строка, содержащая информацию о книге, включая её идентификатор, название, автора, год выпуска, статус
            и количество.
        """
        return (f"ID: {self.book_id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, "
                f"Статус: {self.status}, Количество: {self.count}")

    def to_dict(self) -> dict:
        """
        Возвращает представление книги в виде словаря.

        Возвращает:
            dict: Словарь, где ключи - атрибуты книги, а значения - соответствующие данные.
        """
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
            "count": self.count,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Создает объект книги из словаря.

        Аргументы:
            data (dict): Словарь, содержащий данные книги (например, "id", "title", "author", "year", "status",
            "count").

        Возвращает:
            Book: Новый объект книги, созданный из данных словаря.
        """
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
            count=data["count"],
        )
