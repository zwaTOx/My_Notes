import sqlite3
import os
import datetime

# Определяем путь к файлу базы данных
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'data', 'my_notes.db')

# Устанавливаем соединение с базой данных
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Создаем тестовую таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS Notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

adding_note = 'INSERT INTO Notes (title, description, date, time) VALUES (?, ?, ?, ?);'

#Тестовое наполнение базы данных
cursor.execute(adding_note, ('My Note', 'This is a description', datetime.datetime.now().date().isoformat(), datetime.datetime.now().time().isoformat()))

#Вывод в обратном порядке (Для плашек на главном экране)
cursor.execute('SELECT * FROM Notes ORDER BY ID DESC')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

# Выводим абсолютный путь для файла my_notes.db
print(db_path)
