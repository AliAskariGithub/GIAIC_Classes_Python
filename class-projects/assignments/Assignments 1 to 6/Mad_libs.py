def get_input(prompt):
    return input(prompt).strip()

def play_mad_libs():
    print("\n=== Welcome to Mad Libs Game! ===\n")
    
    noun1 = get_input("Enter a noun: ")
    adjective1 = get_input("Enter an adjective: ")
    verb1 = get_input("Enter a verb: ")
    adverb1 = get_input("Enter an adverb: ")
    noun2 = get_input("Enter another noun: ")
    
    story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}.
    One day, while {verb1}ing, they found a magical {noun2} and lived happily ever after!
    """
    
    print("\n=== Your Mad Libs Story ===")
    print(story)
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_mad_libs()

if __name__ == "__main__":
    play_mad_libs()