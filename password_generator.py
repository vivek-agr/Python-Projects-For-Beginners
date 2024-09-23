import string
import random

def generate_pwd(min_length, number = True, special_char = True):
    # Create letters, digits, special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Add digits, special characters based on condition
    characters = letters
    if number:
        characters += digits
    if special_char:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special_char = False
    
    
    while len(pwd) < min_length or not meets_criteria:
        # Generate random character and add to password
        random_char = random.choice(characters)
        pwd += random_char

        # Check if random character satisfy number and special character condition
        if random_char in digits:
            has_number = True
        elif random_char in special:
            has_special_char = True

        # Check if criteria is met based on givn condition
        meets_criteria = True
        if number:
            meets_criteria = has_number
        if special_char:
            meets_criteria += has_special_char

    return pwd   

# Ask user to set criteria/condition for password generation
min_length = int(input("Enter the length of password to be generated: "))
number = input("Do you want to have numbers (y/n): ").lower() == "y"
special_char = input("Do you want to have special characters (y/n): ").lower() == "y"

# Function call
pwd = generate_pwd(min_length, number, special_char)
print("The generated password is:", pwd)