import datetime

current_date = datetime.datetime.now()

name = input('Name: ')
age = int(input('Age: '))
times_to_display = int(input('How many times do you want to repeat the message: '))

def determine_age_100(age, current_date):
    year = 0
    current_year = current_date.year
    if age == 100:
        year = current_year
    else:
        year = 100 - age
        year = current_year + year
    return year

age_100 = determine_age_100(age, current_date)

message = f'Hello, {name}, your age is {age}, and you will be a hundred years old in {age_100}'

if times_to_display > 0:
    for i in range(times_to_display):
        print(message)
else:
    print(message)