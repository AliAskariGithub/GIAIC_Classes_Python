print("\n -------------------------------- This is the Wholesome Affirmation Machine Program --------------------------------")

def get_affirmation():
    AFFIRMATION = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation: {AFFIRMATION}")
    
    while True:
        user_input = input()
        if user_input == AFFIRMATION:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.")
            print(f"Please type the following affirmation: {AFFIRMATION}")

def main():
    get_affirmation()

if __name__ == '__main__':
    main()

print("\n -------------------------------- Thank you for using program --------------------------------")