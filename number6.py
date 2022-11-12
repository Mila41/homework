# Есть словарь песен
# Раcпечатайте общее время звучания трех случайных песен в формате
# Три песни звучат ххх минут
import random as r
from random import sample
from random import randint

my_favorite_songs = {
    "wast a moment": "3.03",
    "new salvation": "4.02",
    "staying alive": "3.40",
    "out of touch": "3.03",
    "a sorta fairytale": "5.28",
    "easy": "4.15",
    "beautiful day": "4.04",
    "nowhere to run": "2.58",
    "in this world": "4.02",
}
# result = r.choice(my_favorite_songs)
data = list(my_favorite_songs.items())
i = r.sample(data, 3)
key, value = data[randint(0, len(my_favorite_songs)-1)]
print(key, value)
# print('Три песни звучат: ', sum(i))

