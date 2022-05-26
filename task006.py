#  Создайте программу, которая будет играть в игру “коровы и быки” 
# с пользователем. Игра работает так:

# Случайным образом генерируйте 4-значное число. 
# Попросите пользователя угадать 4-значное число. 
# За каждую цифру, которую пользователь правильно угадал в нужном месте, 
# у них есть “корова”. За каждую цифру, которую пользователь угадал правильно, 
# в неправильном месте стоит “бык”. Каждый раз, 
# когда пользователь делает предположение, скажите им, 
# сколько у них “коров” и “быков”. Как только пользователь угадает 
# правильное число, игра окончена. Следите за количеством догадок, 
# которые пользователь делает на протяжении всей игры, 
# и сообщите пользователю в конце.

import random

def get_random_number(length):
    numbers = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    random_number = 0
    for i in range(0, len(numbers)):
        i = random.randint(0, 9)
        while (len(str(random_number)) < length) and (numbers[i] == 0):
            random_number *= 10
            random_number += i
            numbers[i] = 1
    return random_number
    

def bulls_and_cows(rand_number):
    rand_number = str(rand_number)
    guessed_number = ''
    count = 0
    print(f'Угадайте 4х значное число')
    while (guessed_number != rand_number):
        # print(f'Угадайте 4х значное число')
        guessed_number = input()
        while (guessed_number.isnumeric() != True) \
        or (int(guessed_number) > 9999) \
        or (int(guessed_number) < 1000) \
        or (guessed_number[0] == guessed_number[1]) \
        or (guessed_number[0] == guessed_number[2]) \
        or (guessed_number[0] == guessed_number[3]) \
        or (guessed_number[1] == guessed_number[2]) \
        or (guessed_number[1] == guessed_number[3]) \
        or (guessed_number[2] == guessed_number[3]):
            print(f'Введите 4х значное число из неповторяющихся цифр')
            guessed_number = input()
        cow = 0
        bull = 0
        for i in range(0, len(rand_number)):
            for j in range(0, len(guessed_number)):
                #print(f"i = {i}, rand_number[i] = {rand_number[i]}")
                #print(f"j = {j}, guessed_number[j] = {guessed_number[j]}")
                if (rand_number[i] == guessed_number[j]) and (i == j):
                    cow += 1
                elif (rand_number[i] == guessed_number[j]) and (i != j):
                    bull += 1
        count += 1
        print(f'Коровы = {cow}, быки = {bull}')
    print(f"Вы угадали! Количество попыток - {count}")


random_number = get_random_number(4)
print(random_number)
bulls_and_cows(random_number)
