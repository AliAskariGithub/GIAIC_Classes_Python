import random
import string

def load_words():
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 
             'network', 'software', 'developer', 'coding', 'engineer']
    return words

def get_word():
    words = load_words()
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [  # Final state: head, body, both arms, both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # Head, body, both arms, one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # Head, body, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # Head, body, one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # Head and body
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # Head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # Initial state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    tries = 6

    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and tries > 0:
        print(f"\nYou have {tries} tries left.")
        print("Used letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(tries))
        print("Current word:", " ".join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                tries -= 1
                print(f"Letter {guess} is not in the word.")
        elif guess in used_letters:
            print("You already used that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter.")

    if tries > 0:
        print(f"\nCongratulations! You guessed the word {word}!")
    else:
        print(f"\nSorry, you ran out of tries. The word was {word}.")

if __name__ == "__main__":
    while True:
        play_game()
        if input("Play again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")