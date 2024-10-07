import sqlite3


def initiate_db():
    """Создает базу данных и таблицу Users при первом запуске."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INT NOT NULL
    );
    ''')
    connection.commit()
    connection.close()


def initiate_product(title, description, price):
    """Добавляет новый продукт в таблицу Users."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Вставляем продукт в таблицу
    cursor.execute('INSERT INTO Users (title, description, price) VALUES (?, ?, ?)',
        (title, description, price))
    connection.commit()
    connection.close()


def get_all_products():
    """Возвращает все записи из таблицы Users."""
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users')

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
        ("Ultra", "Восстановливающий комплекс", 2561),
        ("Magne", "Магний для мужчин", 500),
    ]

    for product in products_info:
        initiate_product(product[0], product[1], product[2])


# Вызов функции для настройки базы данных (один раз при первом запуске)
setup_database()

# Пример получения всех продуктов
all_products = get_all_products()
