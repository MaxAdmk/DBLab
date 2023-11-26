# create_db.py
from my_project import create_app, db

def create_database():
    print("Ініціалізація додатка...")
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://root:23436703@localhost:5000/DiscordDB',
        # Інші конфігураційні параметри
    }, {
        # Інші додаткові конфігураційні параметри
    })
    print("Додаток ініціалізовано.")

    print("Створення контексту додатка...")
    with app.app_context():
        print("Контекст додатка створено.")

        print("Створення всіх таблиць...")
        db.create_all()
        print("Всі таблиці створено.")

if __name__ == '__main__':
    print("Виклик create_database()...")
    create_database()
    print("create_database() викликано.")
