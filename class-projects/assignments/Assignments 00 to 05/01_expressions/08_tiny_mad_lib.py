print("\n -------------------------------- This is the Program for Tiny Mad Lib --------------------------------")

SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"
# adjective noun verb
def main():
    adjective : str = input("\n\t Please Enter an Adjective and press Enter: ")
    noun : str = input("\n\t Please Enter a Noun and press Enter: ")
    verb : str = input("\n\t Please Enter a Verb and press Enter: ")
    
    print(f"\n\t {SENTENCE_START} {adjective} {noun} {verb}!")
    
if __name__ == '__main__':
    main()
    
print("\n -------------------------------- Thank you for using the Program --------------------------------")