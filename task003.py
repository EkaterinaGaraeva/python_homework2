# В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_difference(list_of_numbers):
    diff = 0
    list_of_fractional_part = []
    for i in list_of_numbers:
        list_of_fractional_part.append(i - int(i))
    max = list_of_fractional_part[0]
    min = list_of_fractional_part[0]
    for j in range(0, len(list_of_fractional_part) - 1):
        if max < list_of_fractional_part[j]:
            max = list_of_fractional_part[j]
    for k in range(0, len(list_of_fractional_part) - 1):
        if min > list_of_fractional_part[k]:
            min = list_of_fractional_part[k]
    max = round(max, 2)
    min = round(min, 2)
    print(f'Разница между максимальным значением дробной части {max} и минимальным значением дробной части {min} равна {max - min}')


new_list = [1.1, 1.2, 3.1, 5, 10.01]
find_difference(new_list)