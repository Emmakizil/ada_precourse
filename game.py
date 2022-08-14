RANGE_LOW=1
RANGE_HIGH=10
def get_number_from_user():
    valid_input = False
    user_input = None
    while not valid_input:
        user_input_string = input("Guess the number: ")

        if user_input_string.isnumeric():
            user_input = int(user_input_string)
            valid_input = True
        else:
            print("You must input a number!")
    
    return user_input


def guess_the_number():
    random_number = random.randint(RANGE_LOW, RANGE_HIGH)

    waiting_for_correct_guess = True
    while waiting_for_correct_guess:
        user_input = get_number_from_user()

        if user_input < RANGE_LOW or user_input > RANGE_HIGH:
            print(f"Your guess is out of bounds.")
            print(f"It must be between {RANGE_LOW} and {RANGE_HIGH}")
        elif user_input == random_number:
            print("You guessed the number!  Good job!")
            waiting_for_correct_guess = False
        elif user_input > random_number:
            print("Your guess is too high")
        elif user_input < random_number:
            print("Your guess is too low")