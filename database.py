import psycopg2
import psycopg2.extras
from config import *
a = []
data = []

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name)
    connection.autocommit = True
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print('ok')

    with connection.cursor() as cursor:

        def sel_all():
            all = []
            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from notes"
                )
                for i in cursor.fetchall():
                    all.append(i[1])
            return all


        def get_title(title):
            with connection.cursor() as cursor:
                cursor.execute(f"select * from notes where notes.title='{title}';")
                return cursor.fetchall()


        def update(data):
            print(data)
            with connection.cursor() as cursor:
                cursor.execute(f"update notes set title='{data[1]}', note='{data[2]}' where notes.id='{data[0]}';")


        def add(data):

            print(data)
            with connection.cursor() as cursor:
                cursor.execute("select notes.id from notes;")
                for i in cursor.fetchall():
                    if data[0] == i:
                        print('sorry')
                    else:
                        cursor.execute(f"insert into notes (id, title, note) values ({data[0]}, '{data[1]}', '{data[2]}');" )


except Exception as _ex:
    print(_ex)

print(sel_all())