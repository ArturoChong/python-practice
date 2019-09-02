a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def get_number():
    number = 0
    number = int(input('Number: '))
    return number

def filter_list_for_number(list, number):
    result = []
    for item in list:
        if item < number:
            result.append(item)    
    return result

number = get_number()
result = filter_list_for_number(a, number)
print(result)