import sqlite3

db = sqlite3.connect('cinema.db')
cur = db.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, genre TEXT);
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY, 
    user_id INTEGER, 
    movie_id INTEGER, 
    rating INTEGER
);

INSERT INTO users (name) VALUES ('Ermek'), ('Alice'), ('Bob'), ('Charlie'), ('Diana');
INSERT INTO movies (title, genre) VALUES 
    ('Inception', 'Sci-Fi'), ('The Dark Knight', 'Action'), 
    ('Interstellar', 'Drama'), ('Pulp Fiction', 'Crime'), 
    ('The Matrix', 'Sci-Fi'), ('Unrated Movie', 'Action');

INSERT INTO reviews (user_id, movie_id, rating) VALUES 
    (1,1,10), (1,2,9), (2,1,8), (3,2,10), (3,5,9), 
    (4,3,8), (4,4,6), (5,5,10), (5,1,9), (2,4,7);
''')

print("- Имя + Фильм + Оценка -")
cur.execute('''
    SELECT u.name, m.title, r.rating 
    FROM reviews r
    JOIN users u ON r.user_id = u.id
    JOIN movies m ON r.movie_id = m.id
''')
for row in cur.fetchall(): print(row)

print("\n- Все фильмы (даже без отзывов) -")
cur.execute('''
    SELECT m.title, r.rating 
    FROM movies m
    LEFT JOIN reviews r ON m.id = r.movie_id
''')
for row in cur.fetchall(): print(row)
print("\n- Статистика -")
cur.execute('SELECT AVG(rating), MAX(rating), MIN(rating) FROM reviews')
stats = cur.fetchone()
print(f"Средняя: {round(stats[0], 2)}, Макс: {stats[1]}, Мин: {stats[2]}")

db.commit()
db.close()