import random
import string

while True:

    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Password must be at least 8 characters.")
        continue

    characters = ""

    upper = input("Include uppercase? (yes/no): ")
    lower = input("Include lowercase? (yes/no): ")
    numbers = input("Include numbers? (yes/no): ")
    symbols = input("Include symbols? (yes/no): ")

    selected = []

    if upper == "yes":
        selected.append(string.ascii_uppercase)

    if lower == "yes":
        selected.append(string.ascii_lowercase)

    if numbers == "yes":
        selected.append(string.digits)

    if symbols == "yes":
        selected.append(string.punctuation)

    if len(selected) < 2:
        print("Select at least two character types.")
        continue

    password = []

    for group in selected:
        password.append(random.choice(group))

    characters = "".join(selected)

    for i in range(length - len(password)):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("Generated Password:", "".join(password))

    again = input("Generate another? (yes/no): ")

    if again != "yes":
        break
    