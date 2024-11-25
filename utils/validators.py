from typing import Callable


def validate_input(prompt: str, validation_func: Callable, error_message: str = None) -> str | int:
    """
    Выполняет валидацию пользовательского ввода с использованием заданной функции валидации.

    Аргументы:
        prompt (str): Сообщение, отображаемое пользователю для ввода.
        validation_func (Callable): Функция, используемая для проверки ввода.
        error_message (str, optional): Сообщение об ошибке, отображаемое при некорректном вводе. Если не указано,
        используется сообщение из исключения.

    Возвращает:
        str | int: Проверенное и валидированное значение.

    Исключения:
        ValueError: Возникает, если ввод не соответствует критериям валидации.
    """
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
    """
    Валидирует название книги.

    Аргументы:
        title (str): Название книги для проверки.

    Возвращает:
        str: Проверенное название книги.

    Исключения:
        ValueError: Возникает, если название пустое или превышает 100 символов.
    """
    if not title:
        raise ValueError("Название книги не может быть пустым.")
    if len(title) > 100:
        raise ValueError("Название книги не должно превышать 100 символов.")
    return title


def validate_author(author: str) -> str:
    """
    Валидирует имя автора книги.

    Аргументы:
        author (str): Имя автора для проверки.

    Возвращает:
        str: Проверенное имя автора.

    Исключения:
        ValueError: Возникает, если имя пустое, превышает 50 символов или содержит недопустимые символы.
    """
    if not author:
        raise ValueError("Имя автора не может быть пустым.")
    if len(author) > 50:
        raise ValueError("Имя автора не должно превышать 50 символов.")
    if not all(char.isalpha() or char.isspace() for char in author):
        raise ValueError("Имя автора должно содержать только буквы и пробелы.")
    return author


def validate_year(year: str) -> int:
    """
    Валидирует год издания книги.

    Аргументы:
        year (str): Год издания в виде строки для проверки.

    Возвращает:
        int: Проверенный год издания.

    Исключения:
        ValueError: Возникает, если год пустой, не является числом или выходит за пределы от 1 до текущего года.
    """
    if not year:
        raise ValueError("Год издания не может быть пустым.")

    try:
        year = int(year)
    except ValueError:
        raise ValueError("Год издания должен быть числом.")

    if not 0 < year <= 2024:
        raise ValueError("Год издания должен быть в пределах от 0 до текущего года.")
    return year


def validate_id(num_id: str) -> int:
    """
    Валидирует идентификатор книги.

    Аргументы:
        num_id (str): Идентификатор книги в виде строки для проверки.

    Возвращает:
        int: Проверенный идентификатор.

    Исключения:
        ValueError: Возникает, если идентификатор не является числом.
    """
    try:
        num_id = int(num_id)
    except ValueError:
        raise ValueError("ID должен быть числом.")

    return num_id
