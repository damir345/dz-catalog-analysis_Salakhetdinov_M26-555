import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# First part

def average_rating(movies):
    '''
    Функция average_rating(movies) возвращает среднюю оценку по каталогу, округленную до одного знака (round).
    '''
    ratings = []
    for movie in movies:
        if 'rating' in movie and movie['rating'] is not None:
            ratings.append(movie['rating'])
    if len(ratings) == 0:
        return None
    avg = sum(ratings) / len(ratings)
    return round(avg, 1)

def catalog_age_stats(movies, current_year=2026):
    if not movies: 
        return (0, 0, 0)
    ages = [current_year - movie['year'] for movie in movies]
    oldest_age = max(ages)
    newest_age = min(ages)
    average_age = sum(ages) / len(ages)
    average_age_rounded = math.ceil(average_age)
    return (oldest_age, newest_age, average_age_rounded)

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

# Second part

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"

    # тернарный оператор
    elif rating >= 7:
        result = "почти шедевр" if rating > 8.5 else "хорошо"
        return result
    
    elif rating >= 5:
        return "средне"
    
    else:
        return "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        
        # средний диапазон
        case _ if 2015 <= year <= 2020:
            return "недавние"
        
        case _:
            return "старые"



def main():
    print("Hello from dz-catalog-analysis-salakhetdinov-M26-555!")


if __name__ == "__main__":
    main()

###outputs
output = average_rating(movies)
print(f'Средняя оценка по каталогу: {output}')
print(catalog_age_stats(movies, 2026))
print(duration_in_hours(136))
print(decade_label(2001))

