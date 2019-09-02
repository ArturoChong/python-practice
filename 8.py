
def get_choice(player):
    choices = ['rock', 'paper', 'scissors',]
    choice = ''

    while choice not in choices: 
        choice = input(f'{player}\'s choice: ').lower()

    return choice

def determine_if_win(choices):
    choice_wins = False

    if choices[0] == 'rock' and choices[1] == 'scissors':
        choice_wins = True
    elif choices[0] == 'scissors' and choices[1] == 'paper':
        choice_wins = True
    elif choices[0] == 'paper' and choices[1] == 'rock':
        choice_wins = True

    return choice_wins 

def game():
    players = ['Player 1', 'Player 2'] 
    print('Rock, Paper, Scissors')
    first_choice = get_choice(players[0])
    second_choice = get_choice(players[1])

    choices = []
    choices.append(first_choice)
    choices.append(second_choice)

    player_1_wins = determine_if_win(choices)

    if player_1_wins:
        print('Player 1 wins.')
    else:
        print('Player 2 wins.')


game()