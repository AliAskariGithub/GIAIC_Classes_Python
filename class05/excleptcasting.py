def main():
    num1 = input("Enter the First Number: ")
    num2 = input("Enter the Second Number: ")
    try:
        result = num1 / num2
    except TypeError:
        print("This is the Type Error.")
    except ValueError:
        print("0 cannot be divided by any number.")
    else:
        print(f"Result has been print successfully: {result}")
        return result
    finally:
        print("Program End")
        
if __name__ == "__main__":
    main()