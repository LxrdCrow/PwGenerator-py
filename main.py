import random as rd
import string

def generate_strong_password(length, use_upper, use_lower, use_digits, use_punct):
    characters = ''
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(rd.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password.append(rd.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password.append(rd.choice(string.digits))
    if use_punct:
        characters += string.punctuation
        password.append(rd.choice(string.punctuation))

    while len(password) < length:
        password.append(rd.choice(characters))
    
    rd.shuffle(password)
    return ''.join(password)


def save_password(filename, password):
    try:
        with open(filename, 'a') as file:
            file.write(password + "\n")
    except Exception as e:
        print(f"Error saving password: {e}")

def main_password():
    input("Press Enter to start...")

    while True:
        try:
            length = int(input("Enter password length (default 12): ") or 12)
            if length < 1:
                raise ValueError("Length must be >= 1")
        except ValueError as e:
            print(f"Invalid input: {e}. Using 12.")
            length = 12

        include_uppercase = input("Include uppercase? (y/n): ").strip().lower() == 'y'
        include_lowercase = input("Include lowercase? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        include_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

        if not (include_uppercase or include_lowercase or include_digits or include_punctuation):
            print("At least one char type must be selected. Using all.")
            include_uppercase = include_lowercase = include_digits = include_punctuation = True

        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_punctuation:
            characters += string.punctuation

        password = generate_strong_password(
            length,
            include_uppercase,
            include_lowercase,
            include_digits,
            include_punctuation
        )

        print(f"\nGenerated password: {password}")

        save_password("passwords.txt", password)
        print("Password saved to passwords.txt")

        again = input("\nGenerate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main_password()

    