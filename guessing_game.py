from random import randint

print('Welcome to Guessing Game!', "It's a good day to play", sep='\n')

while True:
    attempts = 0  # Number of attempts

    # Set maximum number
    print('Do you want to set a maximum number?')
    answer = input('Enter - Yes/No: ')

    if answer.lower() == 'yes':
        while True:
            max_num = input('Enter maximum number: ')
            if max_num.isdigit() and int(max_num) > 1:
                n = randint(1, int(max_num))
                break
            else:
                print('Please enter a number greater than 1')
    else:
        print('Hmm... Then let it be 100)')
        n = randint(1, 100)

    # Main game loop
    while True:
        user_input = input('Enter a number: ')

        # Check if input is a number
        if not user_input.isdigit():
            print('\nOops, it seems this is not a number :)')
            continue

        num = int(user_input)
        attempts += 1

        # Check if user guessed the number
        if num < n:
            print('Your number is less than the target, try again')
        elif num > n:
            print('Your number is greater than the target, try again')
        else:
            print(f'You guessed it, congratulations!\nNumber of attempts: {attempts}')
            break

    # Ask user if they want to play again
    print('Do you want to play again?')
    answer = input('Enter - Yes/No: ')

    if answer.lower() != 'yes':
        print('Thank you for playing the number guessing game. See you again...')
        break