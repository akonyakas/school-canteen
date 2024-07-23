import streamlit as st
import pandas as pd
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Ingredient
from populate import populate_db

# Ensure the database is populated on first deployment
populate_db()

# Function to fetch all ingredients
def get_ingredients():
    db = SessionLocal()
    ingredients = db.query(Ingredient).all()
    db.close()
    return ingredients

# Function to update ingredients in the database
def update_ingredients(dataframe):
    db = SessionLocal()
    try:
        # Clear existing data
        db.query(Ingredient).delete()
        db.commit()
        # Insert updated data
        for _, row in dataframe.iterrows():
            db_ingredient = Ingredient(name=row['Ингредиент'], price=row['Цена'])
            db.add(db_ingredient)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()