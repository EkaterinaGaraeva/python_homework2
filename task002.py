# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import math

def find_product(list_of_numbers):
    list_of_products = []
    for i in range(0, math.ceil(len(list_of_numbers) / 2)):
        list_of_products.append(list_of_numbers[i] * list_of_numbers[len(list_of_numbers) - i - 1])
    print(list_of_products)

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
find_product(list1)
find_product(list2)
