import cal

def main() -> int:
    response : cal.add = cal.add(2, 5)
    assert response ==  5, "Expected 2 + 5 is equal to 5"
    return response

if __name__ == "__main__":
    result = main()
    print(f"Result: {result}")