#  Написать программу преобразования двоичного числа в десятичное.

def conversion_to_decimal(number):
    binar_number = str(number)
    decimal_number = 0
    for i in range(0, len(binar_number)):
        decimal_number += int(number % 10) * 2 ** i
        # print(f'i = {i}')
        # print(decimal_number)
        number /= 10
        # print(number)
    print(f'{binar_number} = {round(decimal_number)}')

conversion_to_decimal(11011011)
