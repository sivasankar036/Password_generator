import random
import string

def generate_passwords(pwlengths):
    passwords = []

    for length in pwlengths:
        password = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)

    return passwords

def replace_with_number(password):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        replace_index = random.randint(0, len(password) - 1)
        password = password[:replace_index] + str(random.randint(0, 9)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    num_replacements = random.randint(1, 2)
    for _ in range(num_replacements):
        replace_index = random.randint(0, len(password) - 1)
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")
    
    password_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i + 1}: "))
        if length < 3:
            length = 3
        password_lengths.append(length)

    passwords = generate_passwords(password_lengths)

    for i, password in enumerate(passwords, 1):
        print(f"Password #{i} = {password}")

if __name__ == "__main__":
    main()
