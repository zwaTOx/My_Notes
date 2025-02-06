import sqlite3
import os
import datetime

class NotesDatabase:
    def __init__(self, name = 'Notes', filename = 'my_notes.db'):
        self.name = name
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(base_dir, 'data', filename)
        self.connection = None
        self.cursor = None

        self.connect()
        self.create_table()
    
    def connect(self):
        #Подключение к базе данных.
        if self.connection is None:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()

    def create_table(self):
        #Создание таблицы, если она не существует.
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{self.name}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        ''')

    def add_note(self, title, description=''):
        #Добавление элемента в базу данных.
        adding_note = f'INSERT INTO {self.name} (title, description, date, time) VALUES (?, ?, ?, ?);'
        self.cursor.execute(adding_note, (title, description, datetime.datetime.now().date().isoformat(), datetime.datetime.now().time().isoformat()))

    def delete_notes(self, *args: int):
        for id in args:
            self.cursor.execute(f'DELETE FROM {self.name} WHERE id = {id}')

    def display_notes(self):
        #Вывод заметок в обратном порядке.
        self.cursor.execute(f'SELECT * FROM {self.name} ORDER BY id DESC')
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close(self):
        #Закрытие соединения с базой данных.
        self.connection.commit()
        self.connection.close()
    
    def drop_database(self):
        #Удаление базы данных
        os.remove(self.path)

if __name__ == "__main__":
    db = NotesDatabase()
    #db.add_note('t2', 'heeey')
    #db.add_note('t1')
    #db.delete_notes(1,2)
    db.display_notes()
    db.close()
    #db.drop_database()
