from .laboratoryWork11Module import *
movies = [
    comedy("1+1", 2011, "Франция", "18+"),
    drama("Зеленая миля", 1999, "США", False, "Справедливость, чудо и человечность"),
    fantastic("Интерстеллар", 2014, "США", 165000000, "Научная фантастика"),
    comedy("Маска", 1994, "США", "6+"),
    drama("Побег из Шоушенка", 1994, "США", False, "Надежда и стойкость духа"),
    fantastic("Матрица", 1999, "США", 63000000, "Киберпанк, научная фантастика")
]

# Выводим информацию о всех фильмах
print("Список всех фильмов:\n")
for film in movies:
    film.get_data()

# Поиск по жанру
search_genre = "Комедия"
print(f"\nФильмы жанра '{search_genre}':")
for film in movies: # Используем film вместо movie
    # Проверяем, что film является экземпляром movie (на всякий случай, хотя список содержит только movie-подобные объекты)
    # и сравниваем жанр
    if isinstance(film, movie) and film.genre.lower() == search_genre.lower():
        film.get_data()

