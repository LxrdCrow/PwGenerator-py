from Gui.logic import generate_strong_password, save_password
import string

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

    