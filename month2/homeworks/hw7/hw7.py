import sqlite3

def init_db():
    with sqlite3.connect('garage_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS parts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        conn.commit()
    print("База данных и таблица 'parts' готовы.")

# 2. CREATE — Добавление товара
def create_part(name, price, quantity):
    with sqlite3.connect('garage_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO parts (name, price, quantity) 
            VALUES (?, ?, ?)
        ''', (name, price, quantity))
        conn.commit()
    print(f"Товар '{name}' успешно добавлен.")



def read_parts():
    with sqlite3.connect('garage_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM parts')
        rows = cursor.fetchall()
        
        print("\n--- Список товаров на складе ---")
        for row in rows:
            print(f"ID: {row[0]} | Название: {row[1]} | Цена: {row[2]}$ | Кол-во: {row[3]}")
        print("--------------------------------\n")




def update_part_price(part_id, new_price):
    with sqlite3.connect('garage_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE parts SET price = ? WHERE id = ?
        ''', (new_price, part_id))
        conn.commit()
    print(f"Цена товара с ID {part_id} обновлена до {new_price}.")

# 5. DELETE — Удаление товара
def delete_part(part_id):
    with sqlite3.connect('garage_store.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM parts WHERE id = ?', (part_id,))
        conn.commit()
    print(f"Товар с ID {part_id} удален.")




if __name__ == "__main__":
    init_db()
    
    create_part("Тормозные колодки", 45.50, 10)
    create_part("Масляный фильтр", 12.00, 25)
    create_part("Свечи зажигания", 8.50, 40)
    
    read_parts()
    
    update_part_price(1, 49.99)
    
    delete_part(2)
 
    read_parts()