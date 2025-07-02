#A guessing game  where the user guesses a secret number

secret_number = 7

guess_count = 0
max_guesses = 3

while guess_count < max_guesses:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    
    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10.")
        continue
    
    guess_count += 1
    
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number!")
        guess_count += 1
        break
    
else:
    print("Wrong guess! Sorry, you've used all your guesses. The secret number was", secret_number)