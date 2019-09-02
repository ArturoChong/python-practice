def is_even(number):
    is_even = False
    if number % 2 == 0:
        is_even = True
    return is_even

def is_multiple_of_four(number):
    is_multiple_of_four = False

    if number % 4 == 0:
        is_multiple_of_four = True
    
    return is_multiple_of_four

def return_message(is_even, is_multiple_of_four, number):
    number_type = 'odd'

    if is_even:
        number_type = 'even'

    message = f'{number} is {number_type}'

    if is_multiple_of_four:
        message += ' and it\'s also a multiple of four.'

    return message

def get_numbers():
    numbers = []

    number_1 = int(input('Number 1: '))
    nubmer_2 = int(input('Number 2: '))

    numbers.append(number_1)
    numbers.append(nubmer_2)

    return numbers

def check_if_number_divides_evenly(numbers):
    divides_evenly = False

    if numbers[0] % numbers[1] == 0:
        divides_evenly = True

    return divides_evenly

def return_message_2(divides_evenly, numbers):
    result = ''

    if divides_evenly:
        result = 'divides evenly'
    else:
        result = 'does not divide evenly'
    
    message = f'{numbers[1]} {result} into {numbers[0]}'

    return message

#is_even = is_even(number)
#is_multiple_of_four = is_multiple_of_four(number)

numbers = get_numbers()
divides_evenly = check_if_number_divides_evenly(numbers)
#message = return_message(is_even, is_multiple_of_four, number)
message = return_message_2(divides_evenly, numbers) 
print(message)



def test_sum():
    assert sum([1,2,3]) == 1, "Should be 6"






print('### TESTS ###')

test_sum()
print("Everything passed")

print('### TESTS ###')
'''
Algorithm

1. Obtain number.
2. Determine if it's even.
    2.1 If number is even, return boolean indicating it's even.
    2.2 If number is odd, return boolean indicating it's odd.
3. Depending on boolean value, alter template message.
4. Print message.
'''