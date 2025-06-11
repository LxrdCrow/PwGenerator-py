import random
import string

def generate_strong_password(length, use_upper, use_lower, use_digits, use_punct):
    characters = ''
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))
    if use_punct:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        raise ValueError("No character sets selected")

    while len(password) < length:
        password.append(random.choice(characters))
    
    random.shuffle(password)
    return ''.join(password)

def save_password(filename, password):
    try:
        with open(filename, 'a') as file:
            file.write(password + "\n")
    except Exception as e:
        raise IOError(f"Error saving password: {e}")

def classify_password_strength(password):
    """
    Simple password strength estimator.
    Returns: 'Weak', 'Medium', or 'Strong'
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_punct = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_punct])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"
