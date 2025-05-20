class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    return "Age is valid"

# Example usage
if __name__ == "__main__":
    try:
        check_age(15)
    except InvalidAgeError as e:
        print(f"Error: {e}")