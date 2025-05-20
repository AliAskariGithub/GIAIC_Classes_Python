import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("Time's up!")

def get_time():
    while True:
        try:
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))
            if minutes >= 0 and 0 <= seconds < 60:
                return minutes * 60 + seconds
            print("Please enter valid time values!")
        except ValueError:
            print("Please enter numbers only!")

def main():
    print("\n=== Countdown Timer ===\n")
    
    while True:
        t = get_time()
        
        print("\nTimer starting...")
        countdown(t)
        
        if input("\nStart another timer? (y/n): ").lower() != 'y':
            break
    
    print("\nThanks for using the timer!")

if __name__ == "__main__":
    main()