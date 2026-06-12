import string
import secrets

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")

    while True:
        user_input = input("Enter password length (min 8 recommended): ").strip()
        try:
            length = int(user_input)
            if length < 1:
                print("Length must be a positive number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    password = generate_password(length)
    print("\nYour secure password: " + password)

    if length < 12:
        print("Tip: For better security, use at least 12-16 characters.")

if __name__ == "__main__":
    main()