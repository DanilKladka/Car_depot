import sys
from PyQt5.QtWidgets import QApplication
from start_page import StartPage

try:
    import mysql.connector
    db_installed = True
except ImportError:
    db_installed = False

if db_installed:
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "12345678",
        "database": "cardepot"
    }

    try:
        connectToDB = mysql.connector.connect(**db_config)

    except mysql.connector.errors.DatabaseError:
        connectToDB = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"]
        )
        cursor = connectToDB.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS cardepot")
        connectToDB.database = "cardepot"

    cursor = connectToDB.cursor()
    cursor.execute("SHOW TABLES LIKE 'details'")
    result = cursor.fetchone()

    if not result:
        
        cursor.execute("""
            CREATE TABLE details (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(30) NOT NULL,
                detailType VARCHAR(30) NOT NULL,
                manufacturer VARCHAR(30) NOT NULL,
                brand VARCHAR(30) NOT NULL,
                model VARCHAR(30) NOT NULL,
                quantity INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            )
        """)

        
        cursor.execute("SELECT COUNT(*) FROM details")
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.executemany("""
        INSERT INTO details (title, detailType, manufacturer, brand, model, quantity, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, [
                ('Колінвал', 'Двигун', 'Nissan', 'Nissan', 'Juke', 10, 10000),
                ('Поршень', 'Двигун', 'Toyota', 'Nissan', 'Juke', 18, 5000),
                ('Сальник клапанів', 'Двигун', 'Nissan', 'Nissan', 'Juke', 0, 5760),
                ('Гальмівні колодки', 'Тормозна система', 'Renault', 'Nissan', 'Juke', 9, 5000),
                ('Вакумний насос', 'Тормозна система', 'Toyota', 'Nissan', 'Juke', 2, 600000),
                ('Масляний насос', 'Двигун', 'Nissan', 'Renault', 'Megane', 5, 3760),
                ('Подушки двигуна', 'Двигун', 'Toyota', 'Renault', 'Megane', 6, 7300),
                ('Фара основна', 'Автосвітло', 'Honda', 'Renault', 'Captur', 15, 2000),
                ('Покажчики повороту', 'Автосвітло', 'Toyota', 'Nissan', 'Juke', 10, 3690),
                ('Коректор фар', 'Автосвітло', 'Ford', 'Nissan', 'X-Trail', 0, 1900),
                ('Масляний насос', 'Двигун', 'Nissan', 'Nissan', 'X-Trail', 8, 3500),
                ('Трос ручника', 'Тормозна система', 'Nissan', 'Nissan', 'X-Trail', 6, 5800)
                ])
            connectToDB.commit()

    cursor.close()
else:
    connectToDB = None 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = StartPage(connectToDB)
    main_window.show()
    sys.exit(app.exec_())
