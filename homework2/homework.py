

# 1. Создать функцию которая создает список
# натуральных чисел от минимума до максимума с шагом
def custom_range(_min, _max, _step=1):
    pass


assert custom_range(1, 4) == [1, 2, 3]
assert custom_range(1, 4, 2) == [1, 3]
assert custom_range(1, 1, 2) == []
print('1 - OK')


# 2. Написать функцию, которая вычисляет факториал заданого числа
def factorial(n):
    pass


assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(20) == 2432902008176640000
print('2 - OK')


# 3. Написать функцию которая определяет
# сколько чисел списка больше по модулю максимального для нахождения модуля
# использовать функцию abs
def count_of_max_numbers(_list):
    pass


assert count_of_max_numbers([]) == 0
assert count_of_max_numbers([1]) == 0
assert count_of_max_numbers([5, 7, -10, -8]) == 2
print('3 - OK')