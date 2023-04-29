# Краткий комментарий к ДЗ OTUS №6

Доброго времени суток.

Собственное ТЗ - работа с реальным API - Google Books API.

- формирование строки запроса из формы ввода приложения
- вывод общей инфо о результатах запроса
- вывод ответа сервера в виде карточек книг с набором данных
- вывод подробного описания отдельной книги
- сохранение отдельных книг для дальнейшей работы по категориям с комментарием
- просмотр собственной библиотеки
- просмотр с сортировкой отдельных книг из собственной библиотеки
- удаление книг из библиотеки
- в дальнейшем - Django + интернет-магазин

Сложности в реализации:

- импорты python - зависят от правильной структура проекта - здесь нужен квалифицированный совет
- pycharm professional в проекте ругается на импорты в /app/database/crud - from database import db, from books.schemas import Book - но все работает отлично
- низкое качество данных, отдаваемых API - /app/gbooks/fetch_data_prepare.py
- ошибки в процессе docker сборки - не хватало uwsgi_buffer_size = 4096, да и 32768 тоже не хватало
- ошибки nginx 502 bad gateway из-за передачи объемных данных через http-протокол
- поскольку в python пришел с react-redux, добавил redis в проект вместо redux - устранил uwsgi, nginx errors
- возможно, есть более простые решения
- инициализация redis в проекте, docker-контейнере
- запись в association tables (many-to-many) в БД /app/database/crud/add_book.py
- хотелось, чтобы ORM автоматически заполнял все таблицы, но пришлось сделать это вручную
- получение данных (many-to-many) - в модели добавил lazy=«selectin», но до конца не разобрался в этом механизме
- выборка данных из БД /app/database/crud/get_books.py - не понятен механизм joined load-subquery
- этот запрос к одной (many-to-many) связи Book.authors возвращает также данные другой (many-to-many) связи  Book.categories и (one-to-one) связи - Book.imd_src. Именно это мне и надо, но непонятна сама магия.
- main.py выглядит очень тяжеловесно, чтобы показать что откуда берется - наверняка можно лучше сделать

Вопросы остались, например не получилось использовать insert on conflict:
<https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#insert-on-conflict-upsert>

```python
    from sqlalchemy.dialects.postgresql import insert

    insert_stmt = insert(my_table).values(
        id='some_existing_id',
        data='inserted value')
    do_nothing_stmt = insert_stmt.on_conflict_do_nothing(
        index_elements=['id']
    )
    print(do_nothing_stmt)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint='pk_my_table',
        set_=dict(data='updated value')
    )
    print(do_update_stmt)
```

Что дальше:

- доработать верстку и внешний вид - он пока простоват, но mobile-compatible благодаря bootstrap
- перенести на Django
- добавить пагинацию
- Добавить интернет-магазин
- и далее . . .

Заранее спасибо за потраченное на проверку время.
Замечания будут очень полезны.

С уваженим, Дмитрий.
