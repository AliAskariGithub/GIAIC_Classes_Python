import requests

def main():
    response = requests.get("https://google.com")
    return response.status_code

if __name__ == "__main__":
    print(main())