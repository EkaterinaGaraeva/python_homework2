# В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''
def find_difference(list_of_numbers):
    list_of_fractional_part = []
    for i in list_of_numbers:
        #if (i - int(i)) != 0:
        #if (type(i) == float):
        if (isinstance(i, float) == True):
            list_of_fractional_part.append(i - int(i))
    max = list_of_fractional_part[0]
    min = list_of_fractional_part[0]
    for j in range(1, len(list_of_fractional_part)):
        if max < list_of_fractional_part[j]:
            max = list_of_fractional_part[j]
    for k in range(1, len(list_of_fractional_part)):
        if min > list_of_fractional_part[k]:
            min = list_of_fractional_part[k]
    max = round(max, 2)
    min = round(min, 2)
    print(f'Разница между максимальным значением дробной части {max} \
    и минимальным значением дробной части {min} равна {round((max - min), 2)}')

def find_difference2(list_of_numbers):
    max = list_of_numbers[0] - int(list_of_numbers[0])
    min = list_of_numbers[0] - int(list_of_numbers[0])
    for j in list_of_numbers:
        if (max < (j - int(j))) and (isinstance(j, float) == True):
            max = j - int(j)
    for k in list_of_numbers:
        if (min > (k - int(k))) and (isinstance(k, float) == True):
            min = k - int(k)
    max = round(max, 2)
    min = round(min, 2)
    print(f'Разница между максимальным значением дробной части {max} \
    и минимальным значением дробной части {min} равна {round((max - min), 2)}')
'''

def find_difference3(list_of_numbers):
    max = list_of_numbers[0] % 1
    min = list_of_numbers[0] % 1
    for j in list_of_numbers:
        if (max < (j % 1)) and (isinstance(j, float) == True):
            max = j % 1
    for k in list_of_numbers:
        if (min > (k % 1)) and (isinstance(k, float) == True):
            min = k % 1
    max = round(max, 2)
    min = round(min, 2)
    print(f'Разница между максимальным значением дробной части {max} \
    и минимальным значением дробной части {min} равна {round((max - min), 2)}')

new_list = [1.1, 1.2, 3.1, 5, 10.01]
#find_difference(new_list)
#find_difference2(new_list)
find_difference3(new_list)
