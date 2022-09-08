# Реализуйте алгоритм перемешивания списка.

import random

def get_list(n, x, y):
    return [random.randint(x, y) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 10
x = 1
y = 20

newlist = get_list(n, x, y)
print(newlist)
shuffle_list(newlist)
print(newlist)