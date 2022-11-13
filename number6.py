# Есть словарь песен
# Раcпечатайте общее время звучания трех случайных песен в формате
# Три песни звучат ххх минут


import random


my_favorite_songs = {
        "wast a moment": 3.03,
        "new salvation": 4.02,
        "staying alive": 3.40,
        "out of touch": 3.03,
        "a sorta fairytale": 5.28,
        "easy": 4.15,
        "beautiful day": 4.04,
        "nowhere to run": 2.58,
        "in this world": 4.02,
    }


r_songs = random.choices(list(my_favorite_songs.values()), k=3)


print(f'Три песни звучат:{r_songs} минут')



