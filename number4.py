# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительность каждого трека
# Выведите общее время звучания трех случайных песен в формате Три песни звучат ххх минут
# Для того, чтобы случайные значения, используйте модуль random import random

import random
from random import sample

my_favorite_songs = (
    ["wast a moment", 3.03],
    ["new salvation", 4.02],
    ["staying alive",3.40],
    ["out of touch", 3.03],
    ["a sorta fairytale", 5.28],
    ["easy", 4.15],
    ["beautiful day", 4.04],
    ["nowhere to run", 2.58],
    ["in this world", 4.02]
)

r_songs = random.choices(my_favorite_songs, k=3)
print(f'Три песни звучат: ', r_songs)