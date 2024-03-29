import random
import string

def generate_password(length, strength):
    characters = {
        'weak': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'strong': string.ascii_letters + string.digits + string.punctuation
    }
    password = ''.join(random.choice(characters[strength]) for i in range(length))
    return password

def get_length():
    while True:
        try:
            length = int(input("\nEnter the length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer")
            return length
        except ValueError as e:
            print("\nInvalid input. Please enter a positive integer for the length.")

def get_strength():
    while True:
        strength = input("\nSelect the strength of the password (weak/medium/strong): ")
        strength = strength.lower()
        if strength in ['weak', 'medium', 'strong']:
            return strength
        print("\nInvalid input. Please select from 'weak', 'medium', or 'strong'.")

def generate():
    while True:
        length = get_length()
        strength = get_strength()

        password = generate_password(length, strength)
        print("\n\nGenerated Password:", password)

        if input("\nDo you want to generate another password? (y/n): ").lower() != 'y':
            break

# Start the password generation process
generate()
