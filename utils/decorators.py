import json


def log_action(func):
    """Логирование вызова функции."""

    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} c аргументами {args[:1]} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def handle_exceptions(func):
    """Логирование ошибок."""

    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except json.JSONDecodeError:
            print("Ошибка при чтении данных из файла.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except FileNotFoundError:
            self.books = []
        except Exception as e:
            print(f"Неопределенная ошибка: {e}")

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def save_after_action(func):
    """Сохранение объекта книги."""

    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.save_books()
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
