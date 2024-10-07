import sqlite3
import os


def initiate_db():
    """Создает базу данных и таблицы при первом запуске."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
    );
    ''')

    # Создаем таблицу Products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL
    );
    ''')

    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Вставляем пользователя в таблицу
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
        (username, email, age))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    connection.close()
    return user is not None


def initiate_product(title, description, price):
    """Добавляет новый продукт в таблицу Products."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Вставляем продукт в таблицу
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
        (title, description, price))
    connection.commit()
    connection.close()


def get_all_products():
    """Возвращает все записи из таблицы Products."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')

    # Получаем все записи и закрываем соединение
    products = cursor.fetchall()
    connection.close()
    return products


# Инициализация базы данных и добавление данных
def setup_database():
    initiate_db()

    products_info = [
        ("ZMA", "Общие витамины", 1125),
        ("Opti", "Универсальный комплекс", 2504),
        ("Ultra", "Восстанавливающий комплекс", 2561),
        ("Magne", "Магний для мужчин", 500),
    ]

    for product in products_info:
        initiate_product(product[0], product[1], product[2])

# Добавил условие для удаления существующего файла .db так как setup создает ее и при каждом новом запуск продуты
# добаляются и дублируются выдавая каждый раз новые картинки
# это условие я использовал для теста и пока писал код по заданию
#if os.path.exists('products.db'):
#    os.remove('products.db')



# Пример получения всех продуктов
all_products = get_all_products()

# Решение для повторной записи products в файл .db пока не знаю на сколько решение верное
if __name__ == '__main__':
    setup_database()
