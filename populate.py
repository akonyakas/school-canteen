from database import engine, SessionLocal, Base
from models import Ingredient

# Create the database and tables
Base.metadata.create_all(bind=engine)

# Default data to be inserted
default_ingredients = [
    {'name': 'Говядина', 'price': 0},
    {'name': 'Говядина мякоть', 'price': 0},
    {'name': 'Горох', 'price': 0},
    {'name': 'Гречка', 'price': 0},
    {'name': 'Капуста', 'price': 0},
    {'name': 'Картофель', 'price': 0},
    {'name': 'Кисель из концентрата', 'price': 0},
    {'name': 'Кислота лимонная', 'price': 0},
    {'name': 'Крупа гречневая', 'price': 0},
    {'name': 'Куриное филе', 'price': 0},
    {'name': 'Курица', 'price': 0},
    {'name': 'Лапша', 'price': 0},
    {'name': 'Лук зеленый', 'price': 0},
    {'name': 'Лук репчатый', 'price': 0},
    {'name': 'Макароны', 'price': 0},
    {'name': 'Масло растительное', 'price': 0},
    {'name': 'Масло сливочное', 'price': 0},
    {'name': 'Молоко', 'price': 0},
    {'name': 'Морковь', 'price': 0},
    {'name': 'Мука пшеничная', 'price': 0},
    {'name': 'Мука пшеничная обогащенная', 'price': 0},
    {'name': 'Рис', 'price': 0},
    {'name': 'Рожки', 'price': 0},
    {'name': 'Сахар', 'price': 0},
    {'name': 'Свекла', 'price': 0},
    {'name': 'Сухари', 'price': 0},
    {'name': 'Сухофрукты', 'price': 0},
    {'name': 'Томатная паста', 'price': 0},
    {'name': 'Укроп', 'price': 0},
    {'name': 'Филе рыбы', 'price': 0},
    {'name': 'Хлеб', 'price': 0},
    {'name': 'Чай', 'price': 0},
    {'name': 'Чай фруктовый', 'price': 0},
    {'name': 'Яблоко', 'price': 0},
    {'name': 'Яйца', 'price': 0},
]

def populate_db():
    db = SessionLocal()
    try:
        # Check if the table is empty
        if not db.query(Ingredient).first():
            for ingredient in default_ingredients:
                db_ingredient = Ingredient(name=ingredient["name"], price=ingredient["price"])
                db.add(db_ingredient)
            db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

# Populate the database with default values if empty
populate_db()