class movie:
    """Родительский класс"""

    def __init__(self, name, year, genre, country):
        self.name = name
        self.year = year
        self.genre = genre
        self.country = country

    def get_data(self):
        """Функция отображения информации о фильме"""
        print(f"Фильм: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Жанр: {self.genre}")
        print(f"Страна: {self.country}")
        print(f"Возраст фильма: {self.calculate_age()} лет")
        self.print_additional_data()
        print("-" * 30)

    def print_additional_data(self):
        pass

    def calculate_age(self):
        return 2025 - self.year

class comedy(movie):
    def __init__(self, name, year, country, rating_age):
        super().__init__(name, year, "Комедия", country)
        self.rating_age = rating_age

    def print_additional_data(self):
        """Вывод дополнительных данных для комедии"""
        print(f"Возрастной рейтинг: {self.rating_age}")


class drama(movie):
    def __init__(self, name, year, country, is_historical: bool, main_theme: str):
        super().__init__(name, year, "Драма", country)
        self.is_historical = is_historical
        self.main_theme = main_theme

    def print_additional_data(self):
        """Вывод дополнительных данных для драмы"""
        print(f"Историческая драма: {'Да' if self.is_historical else 'Нет'}")
        print(f"Основная тема: {self.main_theme}")


class fantastic(movie):
    def __init__(self, name, year, country, special_effects_budget: int, universe_type: str):
        super().__init__(name, year, "Фантастика", country)
        self.special_effects_budget = special_effects_budget
        self.universe_type = universe_type

    def print_additional_data(self):
        """Вывод дополнительных данных для фантастики"""
        print(f"Бюджет на спецэффекты: ${self.special_effects_budget:,}")
        print(f"Тип вселенной: {self.universe_type}")
