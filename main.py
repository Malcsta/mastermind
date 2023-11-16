import random

valid_colours = ['R','G','B','Y','W','O']
interface_active = True
code_length = 4
random_colours = ''
match = None


for i in range(code_length):
    random_colours += random.choice(valid_colours)

code_list = list(random_colours)

def make_guess(user_guess):
    if user_guess in code_list:
        user_guess = code_list.index(user_guess)
        return user_guess


while interface_active:
    
    print('Welcome to mastermind. Guess the 4 colours in the correct places.')
    print('Your colour options are: R G B Y W O')
    choice = input('Enter your 4 digit guess: ')
    choice = choice.upper()
    choice_list = list(choice)
    print(choice_list, code_list)
    for i in choice_list:
        for j in code_list:
            if i == j:
                match = code_list.index(i)
    



