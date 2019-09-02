word = input('Word: ')

def determine_if_palindrome(word):
    return True if word[::-1] == word else False

print(determine_if_palindrome(word))