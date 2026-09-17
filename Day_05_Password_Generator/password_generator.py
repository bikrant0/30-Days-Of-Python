# Password Generator

import random
import string

print("Welcome to The Password Generator!!")

def generate_password():
     
    # Getting password length from user
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Define character pools
    char_pool = string.ascii_letters + string.digits + string.punctuation

    if length < 8:
        print("Password length must be at least 8.")
        return

    # Generate password
    password = "".join(random.choice(char_pool) for _ in range(length))
    
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    generate_password()
