#task 2 Number Guessing Game using import random
import random
secret_number = random.randint(1,100)
print("Guess the number between 1 and 100 !")
while True:
    guess = int(input("Enter the guess : "))
    if guess<secret_number:
        print("Too low ! Try again:")
    elif guess>secret_number:
        print("Too high ! Try again:")
    else:
        print(f"Correct! The number was {secret_number}")
        break
