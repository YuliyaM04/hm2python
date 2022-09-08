# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,округлённую до трёх знаков после точки.

n = int(input('Введите число: ')) 
def get_squerence(n):
    return [round((1 + 1 / x)**x,3) for x in range (1, n + 1)]
nums = get_squerence(n)
print(round(sum(nums), 3))