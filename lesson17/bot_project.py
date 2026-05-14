import sqlite3

conn = sqlite3.connect('bot_user.db', check_same_thread=False)
# check_same_thread = отключает проверку потокобезопасности
cursor = conn.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    city_name TEXT
        )
    ''')
    conn.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city_id INTEGER
    FOREIGN KEY(city_id) REFERENCES cities(id)
        )
    ''')
    conn.commit()

def add_cities():
    cities = ['Warszawa', 'Krakow', 'Gdansk']
    for city in cities:
        cursor.execute('''
        INSERT INTO cities (city_name) VALUES (?)
        ''',(city,))
        conn.commit()

def get_cities():
    cursor.execute('''SELECT * FROM cities''')
    return cursor.fetchall()


def save_user(name, age, city_id):
    cursor.execute('''
        INSERT INTO users (name, age, city_id)
        VALUES (?, ?, ?)
    ''', (name, age, city_id)
    )
    conn.commit()

#JOIN
def get_user_with_cities():
    cursor.execute('''
    SELECT users.name, users.age, users.city_id
    FROM users
    JOIN cities ON users.city_id = cities.id
    ''')
    return cursor.fetchall()


