# Create password generator

import random as rd
import string

def generate_password(length=12, characters=string.ascii_letters + string.digits + string.punctuation):
    """Generate a random password of specified length using selected characters."""
    password = ''.join(rd.choice(characters) for _ in range(length))
    return password

def main_password():
    """Main function to execute the password generation."""
    input("Press Enter to start the password generator...")

    while True:
        try:
            length = int(input("Enter the desired password length (default is 12): ") or 12)
            if length < 1:
                raise ValueError("Length must be at least 1.")
        except ValueError as e:
            print(f"Invalid input: {e}. Using default length of 12.")
            length = 12

        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        include_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

        if not (include_uppercase or include_lowercase or include_digits or include_punctuation):
            print("At least one character type must be selected. Using all types by default.")
            include_uppercase = include_lowercase = include_digits = include_punctuation = True

        # Build character set based on user choices
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_punctuation:
            characters += string.punctuation

        # Generate and display password
        password = generate_password(length, characters)
        print(f"\nGenerated Password: {password}")

        # Ask to continue or exit
        again = input("\nDo you want to generate another password? (y/n): ").strip().lower()
        if again != 'y':
            print("\nExiting the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main_password()

    