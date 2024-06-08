import random
import string


def generate_password(length, lowercase=True, uppercase=True, digits=True, punctuation=True):
    """
    Generates a random password based on user-specified criteria.

    Args:
        length (int): Desired length of the password.
        lowercase (bool, optional): Include lowercase letters (default: True).
        uppercase (bool, optional): Include uppercase letters (default: True).
        digits (bool, optional): Include digits (default: True).
        punctuation (bool, optional): Include punctuation characters (default: True).

    Returns:
        str: The generated password.
    """

    # Define character sets based on user selections
    char_set = ""
    if lowercase:
        char_set += string.ascii_lowercase
    if uppercase:
        char_set += string.ascii_uppercase
    if digits:
        char_set += string.digits
    if punctuation:
        char_set += string.punctuation

    # Generate random password
    password = ''.join(random.sample(char_set, length))
    return password


def main():
    while True:
        try:
            # Get user input for password length
            length = int(input("Enter desired password length (minimum 8 characters): "))
            if length < 8:
                print("Password length must be at least 8 characters. Please try again.")
                continue

            # Get user input for complexity options
            include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
            include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
            include_digits = input("Include digits (y/n)? ").lower() == 'y'
            include_punctuation = input("Include punctuation characters (y/n)? ").lower() == 'y'

            # Generate password
            password = generate_password(length, include_lowercase, include_uppercase, include_digits,
                                         include_punctuation)

            # Display generated password
            print(f"Your generated password is: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter a number for password length.")


if __name__ == "__main__":
    main()
