from typing import Callable


def validate_input(prompt: str, validation_func: Callable, error_message: str = None) -> Callable:
    """Валидация пользовательского ввода."""
    while True:
        value = input(prompt).strip()
        try:
            return validation_func(value)
        except ValueError as e:
            if error_message:
                print(f"Ошибка: {error_message} Попробуйте снова.")
            else:
                print(f"Ошибка: {e} Попробуйте снова.")


def validate_title(title: str) -> str:
    """Валидирует название книги"""
    if not title:
        raise ValueError("Название книги не может быть пустым.")
    if len(title) > 100:
        raise ValueError("Название книги не должно превышать 100 символов.")
    return title


def validate_author(author: str) -> str:
    """Валидирует название книги"""
    if not author:
        raise ValueError("Имя автора не может быть пустым.")
    if len(author) > 50:
        raise ValueError("Имя автора не должно превышать 50 символов.")
    if not all(char.isalpha() or char.isspace() for char in author):
        raise ValueError("Имя автора должно содержать только буквы и пробелы.")
    return author


def validate_year(year: str) -> int:
    """Валидирует год издания книги"""
    if not year:
        raise ValueError("Год издания не может быть пустым.")

    try:
        year = int(year)
    except ValueError:
        raise ValueError("Год издания должен быть числом.")

    if not 0 < year <= 2024:
        raise ValueError("Год издания должен быть в пределах от 0 до текущего года.")
    return year
