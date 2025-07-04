import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    # Define the character sets based on user input
    character_set = ''
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    # Ensure at least one character set is selected
    if not character_set:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password using random.choice
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Get user input for the length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return
    
    # Get user input for the complexity of the password
    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    # Generate the password
    try:
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    except ValueError as ve:
        print(f"Error: {ve}")
        return
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
