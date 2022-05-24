# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def find_sum_of_numbers(list_of_numbers):
    sum = 0
    for i in range(0, len(list_of_numbers), 2):
        sum += list_of_numbers[i]
    return sum

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Сумма чисел списка стоящих на нечетной позиции = {find_sum_of_numbers(new_list)}')
