from unittest.mock import Mock
import json

from utils.decorators import handle_exceptions, save_after_action


# Вспомогательный класс для тестирования декораторов
class HelperLibrary:
    def __init__(self):
        self.books = []
        self.save_books = Mock()  # Мокаем метод save_books

    @handle_exceptions
    def faulty_method(self, raise_exception=None):
        """Метод для тестирования handle_exceptions."""
        if raise_exception:
            raise raise_exception
        return "Success"

    @save_after_action
    def add_book(self, book):
        """Добавляет книгу в список."""
        self.books.append(book)
        return book


def test_handle_exceptions_json_error():
    """Тест обработки json.JSONDecodeError."""
    library = HelperLibrary()
    result = library.faulty_method(raise_exception=json.JSONDecodeError("Error", "", 0))
    assert result is None  # Метод должен возвращать None


def test_handle_exceptions_value_error(capfd):
    """Тест обработки ValueError."""
    library = HelperLibrary()
    result = library.faulty_method(raise_exception=ValueError("Invalid value"))
    captured = capfd.readouterr()
    assert "Ошибка: Invalid value" in captured.out
    assert result is None


def test_handle_exceptions_file_not_found():
    """Тест обработки FileNotFoundError."""
    library = HelperLibrary()
    result = library.faulty_method(raise_exception=FileNotFoundError())
    assert result is None
    assert library.books == []  # Должен быть установлен пустой список


def test_handle_exceptions_general_exception(capfd):
    """Тест обработки любого другого исключения."""
    library = HelperLibrary()
    result = library.faulty_method(raise_exception=RuntimeError("Unexpected error"))
    captured = capfd.readouterr()
    assert "Неопределенная ошибка: Unexpected error" in captured.out
    assert result is None


def test_save_after_action():
    """Тест проверяет, что save_books вызывается после выполнения метода."""
    library = HelperLibrary()
    book = {"title": "Test Book", "author": "Test Author", "year": 2023}

    result = library.add_book(book)

    assert result == book  # Проверяем, что метод возвращает правильный результат
    assert book in library.books  # Проверяем, что книга добавлена
    library.save_books.assert_called_once()  # Проверяем, что save_books был вызван
