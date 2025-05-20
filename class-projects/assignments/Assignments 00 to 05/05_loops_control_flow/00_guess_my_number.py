print("\n -------------------------------- This is the Guess My Number Game Program --------------------------------")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter a guess: "))
            if 0 <= guess <= 99:
                return guess
            print("Please enter a number between 0 and 99")
        except ValueError:
            print("Please enter a valid number")

def play_game():
    import random
    secret_number = random.randint(0, 99)
    print("\nI am thinking of a number between 0 and 99...")
    
    while True:
        guess = get_user_guess()
        
        if guess == secret_number:
            print(f"Congrats! The number was: {secret_number}")
            break
        elif guess < secret_number:
            print("Your guess is too low\n")
        else:
            print("Your guess is too high\n")
        
        print("Enter a new number: ", end="")

def main():
    play_game()

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program --------------------------------")