import random
import string

def generate_random_password(length=12):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choices() function
    password = ''.join(random.choices(characters, k=length))

    return password

if __name__ == "__main__":
    password_length = 12  # You can change the desired length here
    new_password = generate_random_password(password_length)
    print("Generated Password:", new_password)
