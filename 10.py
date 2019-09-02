import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def determine_bigger_list(list1, list2):
    bigger = []

    if len(list1) > len(list2):
        bigger = list1
    else:
        bigger = list2

    return bigger

def generate_random_list(length):
    return [random.randint(0, 100) for item in range(length)]

bigger = determine_bigger_list(a, b)

print(list(set(b).intersection(set(a))))

