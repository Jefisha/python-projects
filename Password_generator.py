import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("The length of the password should be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the password generator
main()
