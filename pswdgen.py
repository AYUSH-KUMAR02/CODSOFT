import random
import string

def generate_password(length):
    # Defining the character sets
    alphabets = string.ascii_letters  # a-z and A-Z
    numbers = string.digits  # 0-9
    special_symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
    
    # List of character sets
    char_sets = [alphabets, numbers, special_symbols]
    
    # Generating the password
    password = ''.join(random.choice(random.choice(char_sets)) for _ in range(length))
    
    return password

# Input from the user
length = int(input("Enter the length of the password: "))
print(f"Generated Password: {generate_password(length)}")
