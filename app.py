"""
Libraring: Консольная система управления библиотекой

Это приложение помогает управлять коллекцией книг, предоставляя функции для добавления, удаления,
поиска и отображения книг. Каждая книга содержит ID, название, автора, год издания и статус
(в наличии или выдана).

Функционал:
- Добавление новых книг с автоматической генерацией ID и статусом "в наличии".
- Удаление книг по ID.
- Поиск книг по названию, автору или году издания.
- Отображение списка всех книг с подробной информацией.
- Изменение статуса книг (в наличии или выдана).

Данные хранятся в JSON-файле для сохранения информации, предусмотрена обработка ошибок.

Приложение разработано с учетом принципов чистого кода и возможности расширения функционала.
"""
from service.runner import Runner

if __name__ == "__main__":
    app = Runner()
    app.run()
