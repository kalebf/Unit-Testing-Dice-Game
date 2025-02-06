import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def get_user_guess():
    while True:
        user_guess = int(input('Guess the total sum (2-12): '))
        if 2 <= user_guess <= 12:
            return user_guess
        else:
            print('Invalid guess. Please enter a number between 2 and 12.')



def check_guess(actual_sum, user_guess):
    if user_guess == actual_sum:
        print(f'Congratulatins! Your guess is correct ({user_guess})')
    elif user_guess < actual_sum:
        print('Too low! Try agian.')
    else:
        print('Too high! Try agian.')
        
def start_game():
    play_again = 'yes'
    actual_sum = roll_dice() 
    while play_again == 'yes' or 'Yes' or 'y' or 'Y':
        for i in range(3):
            user_guess = get_user_guess()
            if user_guess == actual_sum:
                check_guess(actual_sum, user_guess)
                break
            else:
                check_guess(actual_sum, user_guess)
        play_again = input('Do you want to roll again? (yes/no): ')


if __name__ == "__main__":
    start_game()
       
