import roulette

# Get user's data for logging in
def userlogin():

    # Check the user data
    checkDict = {
        "Username": [],
        "Password": [],
        "Money": []
    }

    # Open text file to check if user's username exists
    with open("database.txt", "r") as db:
        read = db.readlines()

        # Delete \n characters
        for data in read:
            u, p, m = data.split(',')
            m = m.strip('\n')

            # Add username, password and money in the lists in checkDict
            checkDict["Username"].append(u)
            checkDict["Password"].append(p)
            checkDict["Money"].append(m)

    # Get user's existing username
    usernameLog = input("Enter your username: ").lower()

    # If username doesn't exist in database, return to logging in
    while usernameLog not in checkDict["Username"]:
        print("This username doesn't exist in our database!\n")
        return userlogin()

    # Index of the Username in checkDict
    index = checkDict["Username"].index(usernameLog)

    # If user doesn't have enough money to play roulette
    for x in checkDict["Money"]:
        converter = int(x)
        while converter < 1:
            print("\n   You can't play on this account anymore,\n"
                  "Because you lost all your money, plase sign in again...")
            exit()

    # Get user's existing password
    passwordLog = input("Enter your password: ").lower()

    # Index of the Password in checkDict according to Username's index
    # Check if the password matches
    while passwordLog != checkDict["Password"][index]:
        print("Password incorrect!\n")
        return userlogin()

    # Appending current user's data to the dict in roulette module
    roulette.currentData["Username"].append(usernameLog)
    roulette.currentData["Password"].append(passwordLog)
    roulette.currentData["Money"].append(checkDict["Money"][index])

    # Send user to roulette game
    roulette.spinWheel()
