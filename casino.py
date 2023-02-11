import random
import time

def dicegame():
    start = input('Type "Start" to start your game: ').lower()
    scoreboard = 0
    win = 0
    loss = 0
    while start != 'start' :
        print('Sorry but you typed the rong word!')
        start = input('Type "Start" to start your game: ').lower()
    while start == 'start':
        x = input('Are you ready for a round? ')
        if x == 'yes':
            user_dice = random.randint(1 ,6)
            computer_dice = random.randint(1, 6)
            print(f'You rolled the dice number -{user_dice}-')
            time.sleep(2)
            print('Waiting for the computer to roll...')
            time.sleep(2)
            print(f'The computer has rolled the number -{computer_dice}-')
            time.sleep(2)
            if user_dice == computer_dice:
                print('You tied with the coomputer!')
            elif user_dice > computer_dice:
                print('You have won against the computer!')
                win = win + 1
            else:
                print('You lost against the computer, have another try!')
                loss = loss + 1
            print(f'Scoreboard: {win}:{loss}')

        else:
            break
    print('Game over!')


def gambling_game():
    money = int(input('How many dollars you wanna start with? '))
    while money > 0:
        correct_number = int(input('Choose a number 1 and 5 to gamble: '))
        roll = random.randint(1, 5)
        if correct_number == roll:
            money = money * 4
            print(f'Congratulations!! Your total now is {money}$!!!')
        elif (roll == correct_number - 1) or (roll == correct_number + 1):
            money = money // 2
            print(f'Oops! you lost half your money! Your total now is {money}$!!!')
        else:
            money = money // 4
            print(f'Oops! you lost money, your total now is {money}$!!!')
    print('Oops! You ran out of money!')


gambling_game()
