import sqlite3
import os

# Определяем путь к файлу базы данных
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'data', 'my_notes.db')

# Устанавливаем соединение с базой данных
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Создаем тестовую таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL
)
''')

# Создаем тестовый индекс для столбца "email"
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

# Выводим абсолютный путь для файла my_notes.db
print(db_path)
