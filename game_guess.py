import random
def guess_number():
    return random.randint(1, 100)

target_number = guess_number()
attempts = 0

while True:
    user_guess = int(input("Enter number: "))
    attempts += 1

    if user_guess == target_number:
        print("Congratulation! You guessed the number in", attempts, "attempts.")
        break
    elif user_guess < target_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")