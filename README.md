libraring
========
<img
  src="https://github.com/Vanxolter/libraring/blob/51df7556078e73b5daebb8fa6bb71f53fbe8fb12/libraring_logo.jpeg"
  alt="libraring"
  width="400"
/>


About
-----
Libraring: Консольная система управления библиотекой

Это приложение помогает управлять коллекцией книг, предоставляя функции для добавления, удаления,
поиска и отображения книг. Каждая книга содержит ID, название, автора, год издания и статус
(в наличии или выдана). Дополнением я решил добавить каунтер для исключения дублирующих записей, теперь при добавлении 
дубликата количество экземпляров книги увеличивается на 1.

Функционал:
- Добавление новых книг с автоматической генерацией ID и статусом "в наличии".
- Удаление книг по ID.
- Поиск книг по названию, автору или году издания (фильтрация по одному или нескольким полям).
- Отображение списка всех книг с подробной информацией.
- Изменение статуса книг (в наличии или выдана).

Данные хранятся в JSON-файле для сохранения информации, предусмотрена обработка ошибок.

Приложение разработано с учетом принципов чистого кода и возможности расширения функционала.

Author: Maksim Laurou <Lavrov.python@gmail.com>

Source link: https://github.com/Vanxolter/libraring

------------------

**ЗАПУСК ПРОЕКТА**

1) Клонируем репозиторий: ``` git clone git@github.com:Vanxolter/libraring.git ```

2) Создаем виртуальное окружение: ``` virtualenv -p python3 --prompt=lib- venv/ ```

3) Устанавливаем необходимые библиотеки (pytest): ``` pip install -r requirements.txt ```

4) Запускаем приложение : ``` python3 app.py ```


------------------

**ТЕСТИРОВАНИЕ ПРОЕКТА**

 ``` pytest ```


