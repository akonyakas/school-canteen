class Ingredient:
    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass

    def __hash__(self):
        return hash(self.name.lower())
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.name.lower() == other.name.lower()
        return False
    
    def __lt__(self, other):
        if isinstance(other, Ingredient):
            return self.name.lower() < other.name.lower()
        return NotImplemented
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class MenuItem:
    def __init__(self, name: str, ingredients: list[Ingredient], portion_size: float):
        self.name = name
        self.ingredients = ingredients
        self.portion_size = portion_size

    def __hash__(self):
        return hash(self.name)

menu = {
    "Неделя 1": {
        "Понедельник": [
            MenuItem(
                "Салат свекольный",
                [
                    Ingredient("Свекла", 121.6),
                    Ingredient("Масло растительное", 3.6),
                ],
                100
            ),
            MenuItem(
                "Гуляш (говядина)",
                [
                    Ingredient("Говядина", 158),
                    Ingredient("Масло растительное", 5),
                    Ingredient("Лук репчатый", 18),
                    Ingredient("Томатная паста", 12),
                    Ingredient("Мука пшеничная", 4),
                ],
                100
            ),
            MenuItem(
                "Гарнир: макароны отварные",
                [
                    Ingredient("Макароны", 66),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ),
            MenuItem(
                "Яблоко",
                [
                    Ingredient("Яблоко", 150),
                ],
                150
            ),
            MenuItem(
                "Хлеб ржано-пшеничный",
                [
                    Ingredient("Хлеб", 40),
                ],
                40
            )
        ],

        "Вторник": [
            MenuItem(
                "Рисовый суп",
                [
                    Ingredient("Говядина", 32),
                    Ingredient("Рис", 6),
                    Ingredient("Лук репчатый", 12),
                    Ingredient("Морковь", 12.5),
                    Ingredient("Картофель", 100),
                ],
                250
            ),
            MenuItem(
                "Кисель",
                [
                    Ingredient("Кисель из концентрата", 20),
                    Ingredient("Сахар", 10),
                    Ingredient("Кислота лимонная", 0.2),
                ],
                200
            ),
        ],

        "Среда" : [
            MenuItem(
                "Салат витаминный",
                [
                    Ingredient("Капуста", 99),
                    Ingredient("Морковь", 10),
                    Ingredient("Лук зеленый", 3),
                    Ingredient("Яблоко", 3),
                    Ingredient("Сахар", 3),
                ],
                100
            ),
            MenuItem(
                "Тефтели мясные (говядина)",
                [
                    Ingredient("Говядина мякоть", 64),
                    Ingredient("Рис", 30),
                    Ingredient("Лук репчатый", 24),
                    Ingredient("Масло растительное", 9),
                    Ingredient("Мука пшеничная обогащенная", 5),
                ],
                100
            ),
            MenuItem(
                "Гарнир: гречка рассыпчатая",
                [
                    Ingredient("Крупа гречневая", 60.6),
                    Ingredient("Масло сливочное", 5.3),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),

        ],
        
        "Четверг" : [
            MenuItem(
                "Салат из моркови",
                [
                    Ingredient("Морковь", 122.2),
                    Ingredient("Сахар", 1),
                    Ingredient("Масло растительное", 5),
                    Ingredient("Укроп", 1),  
                ],
                100
            ),
            MenuItem(
                "Биточки рыбные",
                [
                    Ingredient("Филе рыбы", 69),
                    Ingredient("Хлеб", 15),
                    Ingredient("Яйца", 5),
                    Ingredient("Сухари", 10),  
                    Ingredient("Масло растительное", 7),
                ],
                100
            ),
            MenuItem(
                "Гарнир: картофельное пюре",
                [
                    Ingredient("Картофель", 174.75),
                    Ingredient("Молоко", 24),
                    Ingredient("Масло сливочное", 7.5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),

        ],

        "Пятница" : [
            MenuItem(
                "Суп лапша по домашнему с курицы",
                [
                    Ingredient("Курица", 29),
                    Ingredient("Лапша", 28),
                    Ingredient("Лук репчатый", 30),
                    Ingredient("Масло растительное", 5),  
                    Ingredient("Картофель", 47),
                ],
                250
            ),
        
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай фруктовый", 20),  
                    Ingredient("Сахар", 10),  
                ],
                200
            ),      
        ]
    },

    "Неделя 2": {
        "Понедельник": [
            MenuItem(
                "Салат витаминный",
                [
                    Ingredient("Капуста", 99),
                    Ingredient("Морковь", 10),
                    Ingredient("Лук зеленый", 3),
                    Ingredient("Яблоко", 3),
                    Ingredient("Сахар", 3),
                    Ingredient("Масло растительное", 3),
                ],
                100
            ),
            MenuItem(
                "Плов (говядина)",
                [
                    Ingredient("Говядина", 79.2),
                    Ingredient("Масло растительное", 8),
                    Ingredient("Лук репчатый", 9.6),
                    Ingredient("Морковь", 15.2),
                    Ingredient("Рис", 54.4),
                ],
                200
            ),
            MenuItem(
                "Кисель",
                [
                    Ingredient("Кисель из концентрата", 20),
                    Ingredient("Сахар", 10),
                    Ingredient("Кислота лимонная", 0.5), 
                ],
                200
            ),
    
        ],

        "Вторник": [
            MenuItem(
                "Биточки куриные",
                [
                    Ingredient("Куриное филе", 81.4),
                    Ingredient("Хлеб", 18),
                    Ingredient("Молоко", 24),
                ],
                100
            ),
            MenuItem(
                "Гарнир: рожки",
                [
                    Ingredient("Сухари", 20), 
                    Ingredient("Масло растительное", 6),
                    Ingredient("Рожки", 66),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            )
        ],

        "Среда" : [
            MenuItem(
                "Гороховый суп",
                [
                    Ingredient("Горох", 19),
                    Ingredient("Морковь", 12),
                    Ingredient("Лук репчатый", 12),
                    Ingredient("Говядина", 32),
                    Ingredient("Картофель", 40),
                    Ingredient("Масло растительное", 5),
                ],
                250
            ),
    
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ),
        ],

        "Четверг" : [
            MenuItem(
                "Салат из моркови",
                [
                    Ingredient("Морковь", 107.5),
                    Ingredient("Сахар", 5),
                    Ingredient("Масло растительное", 10.6),
                    Ingredient("Укроп", 5),  
                ],
                100
            ),
            MenuItem(
                "Тефтели рыбные",
                [
                    Ingredient("Филе рыбы", 69),
                    Ingredient("Рис", 13),
                    Ingredient("Лук репчатый", 17),
                    Ingredient("Масло растительное", 8),
                    Ingredient("Мука пшеничная обогащенная", 10), 
                ],
                100
            ),
            MenuItem(
                "Гарнир: картофельное пюре",
                [
                    Ingredient("Картофель", 174.75),
                    Ingredient("Молоко", 24),
                    Ingredient("Масло сливочное", 7.5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),
        ],

        "Пятница" : [
            MenuItem(
                "Салат из свежих овощей",
                [
                    Ingredient("Капуста", 71),
                    Ingredient("Морковь", 36),
                ],
                100
            ),
            MenuItem(
                "Мясо тушеное (курица)",
                [
                    Ingredient("Курица", 85.2),
                    Ingredient("Масло растительное", 6),
                    Ingredient("Лук репчатый", 60),
                    Ingredient("Томатная паста", 11.2),
                    Ingredient("Мука пшеничная", 10), 
                ],
                100
            ),
            MenuItem(
                "Гарнир: гречка",
                [
                    Ingredient("Гречка", 61),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ), 
        ]
    },

    "Неделя 3": {
        "Понедельник": [
            MenuItem(
                "Салат свекольный",
                [
                    Ingredient("Свекла", 121.6),
                    Ingredient("Масло растительное", 3.6),
                ],
                100
            ),
            MenuItem(
                "Гуляш (говядина)",
                [
                    Ingredient("Говядина", 158),
                    Ingredient("Масло растительное", 5),
                    Ingredient("Лук репчатый", 18),
                    Ingredient("Томатная паста", 12),
                    Ingredient("Мука пшеничная", 4),
                ],
                100
            ),
            MenuItem(
                "Гарнир: макароны отварные",
                [
                    Ingredient("Макароны", 66),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ),
        ],

        "Вторник": [
            MenuItem(
                "Рисовый суп",
                [
                    Ingredient("Говядина", 32),
                    Ingredient("Рис", 6),
                    Ingredient("Лук репчатый", 12),
                    Ingredient("Морковь", 12.5),
                    Ingredient("Картофель", 100),
                ],
                250
            ),
            MenuItem(
                "Кисель",
                [
                    Ingredient("Кисель из концентрата", 20),
                    Ingredient("Сахар", 10),
                    Ingredient("Кислота лимонная", 0.5),  
                ],
                200
            ),
        ],

        "Среда" : [
            MenuItem(
                "Салат витаминный",
                [
                    Ingredient("Капуста", 99),
                    Ingredient("Морковь", 10),
                    Ingredient("Лук зеленый", 3),
                    Ingredient("Яблоко", 3),
                    Ingredient("Сахар", 3),
                ],
                100
            ),
            MenuItem(
                "Тефтели мясные (говядина)",
                [
                    Ingredient("Говядина мякоть", 64),
                    Ingredient("Рис", 30),
                    Ingredient("Лук репчатый", 24),
                    Ingredient("Масло растительное", 9),
                    Ingredient("Мука пшеничная обогащенная", 5),
                ],
                100
            ),
            MenuItem(
                "Гарнир: гречка рассыпчатая",
                [
                    Ingredient("Крупа гречневая", 60.6),
                    Ingredient("Масло сливочное", 5.3),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),        
        ],
        
        "Четверг" : [
            MenuItem(
                "Салат из моркови",
                [
                    Ingredient("Морковь", 122.2),
                    Ingredient("Сахар", 1),
                    Ingredient("Масло растительное", 5),
                    Ingredient("Укроп", 5),  
                ],
                100
            ),
            MenuItem(
                "Биточки рыбные",
                [
                    Ingredient("Филе рыбы", 69),
                    Ingredient("Хлеб", 15),
                    Ingredient("Яйца", 5),
                    Ingredient("Сухари", 10),  
                    Ingredient("Масло растительное", 7),
                ],
                100
            ),
            MenuItem(
                "Гарнир: картофельное пюре",
                [
                    Ingredient("Картофель", 174.75),
                    Ingredient("Молоко", 24),
                    Ingredient("Масло сливочное", 7.5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),
           
        ],

        "Пятница" : [
            MenuItem(
                "Суп лапша по домашнему с курицы",
                [
                    Ingredient("Курица", 29),
                    Ingredient("Лапша", 28),
                    Ingredient("Лук репчатый", 30),
                    Ingredient("Масло растительное", 10),  
                    Ingredient("Картофель", 47),
                ],
                250
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай фруктовый", 20),  
                    Ingredient("Сахар", 20),  
                ],
                200
            ),        
        ]
    },

    "Неделя 4": {
        "Понедельник": [
            MenuItem(
                "Салат витаминный",
                [
                    Ingredient("Капуста", 99),
                    Ingredient("Морковь", 10),
                    Ingredient("Лук зеленый", 3),
                    Ingredient("Яблоко", 3),
                    Ingredient("Сахар", 3),
                    Ingredient("Масло растительное", 3),
                ],
                100
            ),
            MenuItem(
                "Плов (говядина)",
                [
                    Ingredient("Говядина", 79.2),
                    Ingredient("Масло растительное", 8),
                    Ingredient("Лук репчатый", 9.6),
                    Ingredient("Морковь", 15.2),
                    Ingredient("Рис", 54.4),
                ],
                200
            ),
            MenuItem(
                "Кисель",
                [
                    Ingredient("Кисель из концентрата", 20),
                    Ingredient("Сахар", 10),
                    Ingredient("Кислота лимонная", 0.5), 
                ],
                200
            ),
        ],

        "Вторник": [
            MenuItem(
                "Биточки куриные",
                [
                    Ingredient("Куриное филе", 81.4),
                    Ingredient("Хлеб", 18),
                    Ingredient("Молоко", 24),
                ],
                100
            ),
            MenuItem(
                "Гарнир: рожки",
                [
                    Ingredient("Сухари", 10),  
                    Ingredient("Масло растительное", 6),
                    Ingredient("Рожки", 66),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),
        ],

        "Среда" : [
            MenuItem(
                "Гороховый суп",
                [
                    Ingredient("Горох", 19),
                    Ingredient("Морковь", 12),
                    Ingredient("Лук репчатый", 12),
                    Ingredient("Говядина", 32),
                    Ingredient("Картофель", 40),
                    Ingredient("Масло растительное", 5),
                ],
                250
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ),       
        ],

        "Четверг" : [
            MenuItem(
                "Салат из моркови",
                [
                    Ingredient("Морковь", 107.5),
                    Ingredient("Сахар", 5),
                    Ingredient("Масло растительное", 10.6),
                    Ingredient("Укроп", 5),  
                ],
                100
            ),
            MenuItem(
                "Тефтели рыбные",
                [
                    Ingredient("Филе рыбы", 69),
                    Ingredient("Рис", 13),
                    Ingredient("Лук репчатый", 17),
                    Ingredient("Масло растительное", 8),
                    Ingredient("Мука пшеничная обогащенная", 10), 
                ],
                100
            ),
            MenuItem(
                "Гарнир: картофельное пюре",
                [
                    Ingredient("Картофель", 174.75),
                    Ingredient("Молоко", 24),
                    Ingredient("Масло сливочное", 7.5),
                ],
                150
            ),
            MenuItem(
                "Компот из смеси сухофруктов",
                [
                    Ingredient("Сухофрукты", 20),
                    Ingredient("Сахар", 20),
                ],
                200
            ),           
        ],

        "Пятница" : [
            MenuItem(
                "Салат из свежих овощей",
                [
                    Ingredient("Капуста", 71),
                    Ingredient("Морковь", 36),
                ],
                100
            ),
            MenuItem(
                "Мясо тушеное (курица)",
                [
                    Ingredient("Курица", 85.2),
                    Ingredient("Масло растительное", 6),
                    Ingredient("Лук репчатый", 60),
                    Ingredient("Томатная паста", 11.2),
                    Ingredient("Мука пшеничная", 0),  
                ],
                100
            ),
            MenuItem(
                "Гарнир: гречка",
                [
                    Ingredient("Гречка", 61),
                    Ingredient("Масло сливочное", 5),
                ],
                150
            ),
            MenuItem(
                "Чай с сахаром",
                [
                    Ingredient("Чай", 1),
                    Ingredient("Сахар", 15),
                ],
                200
            ),      
        ]
    }
}

# ingredients = set()
# for week, days in menu.items():
#     for day, items in days.items():
#         for menu_item in items:
#             for ingredient in menu_item.ingredients:
#                 ingredients.add(ingredient)

# for ingr in sorted(list(ingredients)):
#     print(str({'name': ingr.name, 'price': 0})+',')
    