import random


def random_number_generate():
    """
    For Random number generate function.
    :return:
    """
    number = random.randint(1, 100)
    guessing_game(number)


def guessing_game(jackpot):
    print(jackpot)
    guess_num = int(input("Guess The Number: "))
    count = 1
    for num in range(jackpot):
        # print(num)
        if guess_num == jackpot:
            print(
                f"You Win The Game. You Guess The Number In {count} Attempts")
            print("-----------------------------------------------------"
                  "\n")
            exit_or_not = str(input("If You Want Play Again Type(yes) Or Exit "
                                    "Type(no): "))
            if exit_or_not == 'no':
                print("Thanks For Playing")
                break
            if exit_or_not == 'yes':
                random_number_generate()

            break

        if guess_num > jackpot:
            print("Guess Lower.")
        if guess_num < jackpot:
            print("Guess Higher.")

        guess_num = int(input("Guess The Number: "))
        count += 1


if __name__ == "__main__":
    random_number_generate()
