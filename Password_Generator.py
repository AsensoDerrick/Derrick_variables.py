import random
import string

def password_generator():
    print("=== PASSWORD GENERATOR ===")

    # Step 1: Ask for password length
    while True:
        try:
            length = int(input("Enter desired password length: "))
            if length < 4:
                print("Password should be at least 4 characters long.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Step 2: Ask if user wants special characters
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    # Step 3: Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation if include_special else ""

    # Combine all selected character sets
    all_characters = upper + lower + digits + special

    # Step 4: Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Step 5: Display the password
    print("\nYour generated password is:")
    print(password)

# Run the program
password_generator()

