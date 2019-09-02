import random

def guess():
    keep_going = True 
    number = random.randint(1,9)
    attempts = 0
    choice = ''

    print('Choose a number between 1 and 9. Type exit to stop.')
    while keep_going: 
        attempts += 1
        choice = input('Choice: ')
        if choice.lower() == 'exit':
            keep_going = False 
        try:
            result = determine_if_close(int(choice), number)
            print(f'{choice} is {result}')
            if result == 'exactly equal.':
                keep_going = False
                print(f'You attempted to guess {attempts} times.')
        except:
            pass

    return choice

def determine_if_close(guess, number):
    result = ''

    if guess > number:
        result = 'too high.'
    elif guess < number:
        result = 'too low.'
    else:
        result = 'exactly equal.'

    return result

choice = guess()
