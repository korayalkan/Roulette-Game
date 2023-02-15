import random

# This dict contains our current user's data
currentData = {
                "Username": [],
                "Password": [],
                "Money": []
}

# For red colors
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

# For black colors
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

# For green color
green = [0]

# This is the roulette function
def spinWheel():

    # Take user's money as integer
    global item, balance, userBet, userNumber
    money = currentData["Money"]
    for item in money:
        pass
    converter = int(item)

    # Welcome message
    print("\n")
    print("=-" * 25)
    print("             Welcome to Roulette G!")
    print("-=" * 25)

    # Generate a random number with the help of random library
    winningNum = random.randint(0, 36)
    #print(winningNum)           # For testing, printing the number
    for x in currentData["Money"]:
        print("You have: $"+x)

    # Ask for user's bet with exception handling
    try:
        userBet = int(input("How much do you want to bet?: $"))

    except ValueError:
        print("You can only enter numbers!")
        spinWheel()

    # Bet can't be less than 0
    while int(userBet) <= 0:
        print("Bet can't be 0 or less than 0!\n")
        return spinWheel()

    # Bet can't be higher than user's money
    while int(userBet) > converter:
        print("You don't have enough money!\n")
        return spinWheel()

    # Ask for user's number with exception handling
    try:
        userNumber = int(input("Choose a number to place your bet: "))

    except ValueError:
        print("You can only enter numbers!")
        spinWheel()

    # User's number must be between 0 and 36
    while int(userNumber) > 36:
        print("Your number must be between 0 and 36!\n")
        return spinWheel()

    # User's number must be between 0 and 36
    while int(userNumber) < 0:
        print("Your number must be between 0 and 36!\n")
        return spinWheel()

    # After taking user's bet, delete the bet amount from wallet
    updatedLose = int(converter) - int(userBet)
    currentData["Money"].clear()
    currentData["Money"].append(updatedLose)

    # If user can't guess the winning number
    while int(userNumber) != winningNum:
        print("\nYou couldn't guess Winning Number!\n")

        # Copied and pasted from line 23, same thing
        money = currentData["Money"]
        for item in money:
            pass
        converter = int(item)

        # If user lost his/her all money
        while converter < 1:
            print("You lost all your money,\n"
                  "You can't play on this account anymore.\n"
                  "Please restart the program and sign in again...")

        # Ask user if he/she wants to play again
        playAgain = input("Play Again       |  1\n"
                          "Exit             |  2: ")

        # If user wants to play again
        while int(playAgain) == 1:
            spinWheel()

        while int(playAgain) == 2:
            # Delete user's line from text file
            # Read all the information and delete
            with open("database.txt", "r") as db:
                lines = db.readlines()

            # Delete the specific line in text file
            with open("database.txt", "w") as db:
                for line in lines:
                    for data in currentData["Username"]:
                        if data not in line:
                            db.write(line)

            # Convert it to string to write it to text file
            for balance in currentData["Money"]:
                balance = str(balance)

            # Write updated user's data to text file
            with open("database.txt", "a") as db:
                db.writelines(currentData["Username"])
                db.writelines(',')
                db.writelines(currentData["Password"])
                db.writelines(',')
                db.writelines(balance)
                db.writelines('\n')

            print("\n")
            print("=-" * 25)
            print("        Thanks for playing in Roulette G!")
            print("-=" * 25)
            quit()

        else:
            print("An error has occured!")
            print("Please restart the program...")
            quit()

    # If user guesses the winning number
    while int(userNumber) == winningNum:

        # If the color is red, give the x2 amount of bet
        if int(userNumber) in red:
            redPrize = int(userBet) * 2
            print("\n💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("         Congrats! You won $", redPrize)
            print("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("\n")

            # Give back the bet amount and prize
            redWon = int(redPrize) + int(converter)
            del currentData["Money"][0]
            currentData["Money"].append(redWon)

        # If the color is black, give the x3 amount of bet
        elif int(userNumber) in black:
            blackPrize = int(userBet) * int(3)
            print("\n💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("         Congrats! You won $", blackPrize)
            print("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("\n")

            # Give back the bet amount and prize
            blackWon = int(blackPrize) + int(converter)
            del currentData["Money"][0]
            currentData["Money"].append(blackWon)

        # If the color is green, give the x50 amount of bet
        elif int(userNumber) in green:
            greenPrize = int(userBet) * 50
            print("\n💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("           Congrats! You won $", greenPrize)
            print("💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸💸")
            print("\n")
            print(currentData["Money"])

            # Give back the bet amount and prize
            greenWon = int(greenPrize) + int(converter)
            del currentData["Money"][0]
            currentData["Money"].append(greenWon)

        # Ask user if he/she wants to play again
        print(currentData["Money"])

        # Ask user to play again/exit
        playAgain = input("Play Again       |  1\n"
                          "Exit             |  2: ")

        # If user wants to play again
        while int(playAgain) == 1:
            spinWheel()
            return False

        while int(playAgain) == 2:

            # Delete user's line from text file
            # Read all the information and delete
            with open("database.txt", "r") as db:
                lines = db.readlines()

            # Delete the specific line in text file
            with open("database.txt", "w") as db:
                for line in lines:
                    for data in currentData["Username"]:
                        if data not in line:
                            db.write(line)

            for balance in currentData["Money"]:
                balance = str(balance)

            # Write updated user's data to text file
            with open("database.txt", "a") as db:
                db.writelines(currentData["Username"])
                db.writelines(',')
                db.writelines(currentData["Password"])
                db.writelines(',')
                db.writelines(balance)
                db.writelines('\n')

            print("=-" * 25)
            print("        Thanks for playing in Roulette G!")
            print("-=" * 25)
            quit()
            return False
