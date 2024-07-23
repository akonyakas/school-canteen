import streamlit as st
import pandas as pd
from crud import get_ingredients, update_ingredients
from menu import menu
st.title("Учет Столовых Расходов")

# Model selection
col1, col2 = st.columns(2)
with col1:
    school_name = st.text_input("Напишите название школы")
    number_children = st.number_input("Напишите количество учеников",step = 1)

    # Генерация списка дней в нужном формате (только 1 и 2 недели)
    all_days = []
    for i in range(1, 61):
        week = (i - 1) // 5 % 2 + 1
        day_of_week = (i - 1) % 5
        day_name = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"][day_of_week]
        all_days.append(f"Неделя {week} | {day_name}")

    # Создаем слайдер
    start_day, end_day = st.slider(
        label="Выберите период",
        min_value=1,
        max_value=60,
        value=(1, 60)
    )

    # Получение начального и конечного дня
    start_display, end_display = all_days[start_day - 1], all_days[end_day - 1]

    # Вычисляем количество выбранных дней
    number_of_days = end_day - start_day + 1

    # Отображаем выбранный период
    st.write(f"Вы выбрали период с {start_display} до {end_display}")
    st.write(f"Количество выбранных дней: {number_of_days}")

 
with col2:
    # Streamlit app interface
    st.write("Список ингредиентов")

    # Fetch ingredients from the database
    ingredients = get_ingredients()
    # Convert to DataFrame for editing
    df = pd.DataFrame([ingredient.__dict__ for ingredient in ingredients])

    # make df column order id, name, price
    df = df[['name', 'price']]

    # rename columns
    df.columns = ['Ингредиент', 'Цена']


    # Display editable DataFrame
    edited_df = st.data_editor(df, hide_index=True, use_container_width=True)
    if st.button("Сохранить цены"):
        update_ingredients(edited_df)
        st.success("Изменения сохранены!")
    
    ingredients = get_ingredients()
    ingredient2price = {ingredient.name: ingredient.price for ingredient in ingredients}

ingredients2mass = {}
for day in all_days[start_day-1:end_day]:
    week, day_name = day.split(" | ")
    menu_items = menu[week][day_name]
    for menu_item in menu_items:
        for ingredient in menu_item.ingredients:
            if ingredient.name not in ingredients2mass:
                ingredients2mass[ingredient.name] = 0
            ingredients2mass[ingredient.name] += ingredient.mass

pr = st.button("Расчитать", use_container_width=True)
if pr:
    st.title(f"Расчет стоимости продуктов школы {school_name}")
    main_df = pd.DataFrame(ingredients2mass.items(), columns=["Ингредиент", "Масса на одного (г)"])
    main_df[f'Масса на {number_children} учеников (кг)'] = main_df["Масса на одного (г)"] * number_children / 1000
    main_df['Общая сумма'] = main_df["Масса на одного (г)"] * number_children / 1000 * main_df['Ингредиент'].map(ingredient2price)
    main_df.sort_values(by='Ингредиент', inplace=True)
    st.dataframe(main_df, hide_index=True, use_container_width=True)
    st.success(f'Итого: {main_df["Общая сумма"].sum()}')


