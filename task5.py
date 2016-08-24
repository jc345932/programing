import random


def get_lucky_number():
    rand_number = random.randint(1, 100)
    return rand_number
num1 = get_lucky_number()
num2 = get_lucky_number()
print(num1, num2)