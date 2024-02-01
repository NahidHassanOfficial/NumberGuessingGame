import os
import random
import difficulty_level
import database

# welcome message
print("Welcome to Number Guessing Game\n      Guess the Number\n      Game Starts Now\n\n")


def main():
    """
    The main function for the number guessing game.
    """
    level = difficulty_level.get_difficulty()

    while True:
        secret_number = generate_secret_number(level)
        print(secret_number)
        guess_count = play_round(secret_number)

        show_play_result(guess_count, level)
        database.update_current_tier(level, database.get_current_tier(level)+1)

        if not play_again():
            break

        # verify is current tier limit reached or not!
        level = difficulty_level.difficulty_level_verify(level)

    print("Thanks for playing!")
    database.conn.close()


def generate_secret_number(level):
    if level == "easy":
        return random.randint(1, 50)
    elif level == "medium":
        return random.randint(1, 100)
    else:
        return random.randint(1, 200)


def valid_guess():
    while True:
        try:
            user_guessed = int(input("Enter Number: "))
            return user_guessed
        except ValueError:
            print("Enter a valid number")


def play_round(secret_number):
    guess_counter = 0
    while True:
        user_guessed = valid_guess()
        guess_counter += 1

        if user_guessed != secret_number:
            difference = abs(secret_number - user_guessed)
            if difference > 40:
                print("Not close. Keep guessing! ❄️")
            elif difference <= 4:
                if difference <= 2:
                    print("Burning hot! ")
                else:
                    print("Warm! ")
            else:
                print("I believe in you.")
        else:
            return guess_counter


def show_play_result(guess_count, level):
    highest_score = database.get_highest_score(level)

    print("Cogratulations! you've made it.")
    if highest_score > guess_count:
        highest_score = guess_count
        print(f"Congrats! You have achived highest score with minimum {
              guess_count} guesses")
        database.update_highest_score(level, highest_score)

    elif highest_score == guess_count:
        print(f"You were too close to beat the highest score. your score {
              guess_count} and highest score {highest_score}")

    else:
        print(f"Your score {guess_count} and highest score {highest_score}")


def play_again():
    while True:
        answer = input("Wanna play again? Y/N: ").upper()
        if answer in ("Y", "N"):
            os.system("cls")
            return answer == "Y"
        else:
            print("Invalid answer. Please enter Y or N.")


if __name__ == "__main__":
    main()
