import pytest

from utils.validators import validate_title, validate_author, validate_year, validate_id


# Тесты для validate_title
@pytest.mark.parametrize("title", ["Valid Title", "Another Valid Title", "A" * 100])
def test_validate_title_success(title):
    assert validate_title(title) == title


@pytest.mark.parametrize(
    "title, expected_error",
    [
        ("", "Название книги не может быть пустым."),
        ("A" * 101, "Название книги не должно превышать 100 символов."),
    ],
)
def test_validate_title_errors(title, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        validate_title(title)


# Тесты для validate_author
@pytest.mark.parametrize("author", ["John Doe", "Иван Иванов", "A" * 50])
def test_validate_author_success(author):
    assert validate_author(author) == author


@pytest.mark.parametrize(
    "author, expected_error",
    [
        ("", "Имя автора не может быть пустым."),
        ("A" * 51, "Имя автора не должно превышать 50 символов."),
        ("John123", "Имя автора должно содержать только буквы и пробелы."),
    ],
)
def test_validate_author_errors(author, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        validate_author(author)


# Тесты для validate_year
@pytest.mark.parametrize("year", ["2023", "1", "2024"])
def test_validate_year_success(year):
    assert validate_year(year) == int(year)


@pytest.mark.parametrize(
    "year, expected_error",
    [
        ("", "Год издания не может быть пустым."),
        ("abc", "Год издания должен быть числом."),
        ("-1", "Год издания должен быть в пределах от 0 до текущего года."),
        ("2025", "Год издания должен быть в пределах от 0 до текущего года."),
    ],
)
def test_validate_year_errors(year, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        validate_year(year)


# Тесты для validate_id
@pytest.mark.parametrize("num_id", ["1", "42", "1000"])
def test_validate_id_success(num_id):
    assert validate_id(num_id) == int(num_id)


@pytest.mark.parametrize(
    "num_id, expected_error",
    [
        ("abc", "ID должен быть числом."),
        ("", "ID должен быть числом."),
    ],
)
def test_validate_id_errors(num_id, expected_error):
    with pytest.raises(ValueError, match=expected_error):
        validate_id(num_id)