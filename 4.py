number = int(input('Number: '))

divisors = [item for item in range(1, 10) if number % item == 0]

print(divisors)