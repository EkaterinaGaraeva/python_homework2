# Написать программу преобразования десятичного числа в двоичное

def conversion_to_binary(number):
    decimal_number = number
    binary_number = []
    while decimal_number > 0:
        binary_number.append(decimal_number % 2)
        decimal_number = int(decimal_number / 2)
    size = len(binary_number)
    for j in range(0, int(size / 2)):
        temp = binary_number[j]
        binary_number[j] = binary_number[size - j - 1]
        binary_number[size - j - 1] = temp
    print(f'{number} = {binary_number}')

conversion_to_binary(18)
