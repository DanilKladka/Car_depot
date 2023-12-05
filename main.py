import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication
from start_page import StartPage
import time

def create_database(connection):
    try:
        # Якщо є бд то ми не створюємо 
        cursor = connection.cursor()
        cursor.execute("USE car_depot")
        print("База даних вже існує.")
    except mysql.connector.Error as err:
        # Якщо бд немає то створюємо її
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE car_depot")
            print("База даних створена.")

            cursor.execute("USE car_depot")

            # Створення таблиці details
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
            print("Таблиця details створена.")

            # Додавання початкових значень
            initial_data = [
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
                ('Трос ручника', 'Тормозна система', 'Nissan', 'Toyota', 'Corola', 6, 5800)
            ]

            cursor.executemany("""
                INSERT INTO details (title, detailType, manufacturer, brand, model, quantity, price)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, initial_data)
            print("Додано початкові дані.")

    connection.commit()

if __name__ == '__main__':
    # Підключення до серверу MySQL
    connectToDB = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin"
    )

    # Створення бази даних, таблиці та додавання початкових значень
    create_database(connectToDB)

    # Затримка перед викликом GetCars()
    time.sleep(1)

    # Запуск додатка
    app = QApplication(sys.argv)
    main_window = StartPage(connectToDB)
    main_window.show()
    sys.exit(app.exec_())
