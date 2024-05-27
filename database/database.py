import sqlite3


def create_table(data, another_data):
    try:
        conn = sqlite3.connect('database/DB.db')
        cur = conn.cursor()
        print("Подключение к бд")
        cur.execute(""" CREATE TABLE IF NOT EXISTS main_table (some_collumn TEXT, another_collumn int) """)
        conn.commit()
        print("Таблиц создана")
        insert_data = """ INSERT INTO main_table (some_collumn, another_collumn) VALUES (?, ?) """
        data_tuple = (data, another_data)
        cur.execute(insert_data, data_tuple)
        conn.commit()
        cur.close()
    except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
