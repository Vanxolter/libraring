import pytest


@pytest.mark.parametrize(
    "title, author, year, count",
    [
        ("Book 1", "Author I", 2000, 1),
        ("Book 2", "Author II", 2010, 1),
        ("Book 3", "Author II", 2012, 1),
        ("Book 4", "Author III", 2020, 1),
        ("Book 4", "Author III", 2020, 2),
    ],
)
def test_add_multiple_books(library, title, author, year, count):
    """Тест добавления множества книг в библиотеку."""
    book = library.add_book(title=title, author=author, year=year)

    # Проверяем свойства добавленной книги
    assert book.title == title
    assert book.author == author
    assert book.year == year
    assert book.count == count
    assert book.status == "в наличии"

    # Проверяем состояние библиотеки
    assert book in library.books


def test_find_books(library):
    # Поиск по автору
    books = library.find_books(author="Author II")
    print([book.title for book in books])
    assert len(books) == 2
    assert books[0].title == "Book 2"
    assert books[1].title == "Book 3"

    # Поиск по названию
    books = library.find_books(title="Book 1")
    assert len(books) == 1
    assert books[0].author == "Author I"

    # Поиск по году
    books = library.find_books(year=2012)
    assert len(books) == 1
    assert books[0].title == "Book 3"

    # Поиск по названию, автору и году
    books = library.find_books(title="Book 3", year=2012, author="Author II")
    assert len(books) == 1
    assert books[0].title == "Book 3"

    # Поиск несуществующей книги
    books = library.find_books(title="Nonexistent Book")
    assert len(books) == 0


def test_display_books_true(library):
    books = library.display_books()
    assert books is True


def test_update_status(library):
    # Выдача книги
    result1 = library.update_status(book_id=1, status="выдана")
    assert result1 is True
    assert library.find_book_by_id(1).count == 0

    # Возврат книги
    result2 = library.update_status(book_id=1, status="в наличии")
    assert result2 is True
    assert library.find_book_by_id(2).count == 1


def test_remove_book(library):
    result = library.remove_book(book_id=1)
    assert result is True
    assert len(library.books) == 3

    # Попытка удалить несуществующую книгу
    result = library.remove_book(book_id=999)
    assert result is False

    [library.remove_book(book_id=i) for i in range(2, 5)]


