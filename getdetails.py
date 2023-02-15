import checkdetails
import roulette

# Get user's data for registering
def userregister():

    # In this list, I store the current user's username and password for registering
    userDict = {
                "Username": [],
                "Password": [],
                "Money": []
    }

    # To check user's username if exists
    controlDict = {
                    "Usernames": [],
                    "Passwords": [],
                    "Moneys": []
    }

    # User's starting money
    bonus = "100"

    # Get username
    usernameReg = input("Enter a username: ").lower()

    # Open text file to check if user's username exists
    with open("database.txt", "r") as db:
        read = db.readlines()

        # Delete \n characters
        for data in read:
            u, p, m = data.split(',')
            m = m.strip('\n')

            # Add username, password and money in the lists in controlDict
            controlDict["Usernames"].append(u)
            controlDict["Passwords"].append(p)
            controlDict["Moneys"].append(m)

    # If username already exists
    while usernameReg in controlDict["Usernames"]:
        print("This username exists. Choose another one!\n")
        userregister()

    # Username length must be 5-16 chars long
    while len(usernameReg) < 5:
        print("Username length must be between 5-16 characters long!\n")
        userregister()

    # Username length must be 5-16 chars long
    while len(usernameReg) > 16:
        print("Username length must be between 5-16 characters long!\n")
        userregister()

    # Get the password
    passwordReg = input("Enter your password: ").lower()

    # Password length 6-12 char long
    while len(passwordReg) < 6:
        print("Password length must be between 6-12 characters long!\n")
        userregister()

    # Password length 6-12 char long
    while len(passwordReg) > 12:
        print("Password length must be between 6-12 characters long!\n")
        userregister()

    # Confirm password
    confirmPassword = input("Enter your password again: ").lower()

    # If passwords don't match
    while passwordReg != confirmPassword:
        print("Passwords don't match!\n")
        return userregister()

    # Add username, password and money in dict
    userDict["Username"].append(usernameReg)
    userDict["Password"].append(passwordReg)
    userDict["Money"].append(bonus)

    # Open the text file to write user data
    with open("database.txt", "a") as db:
        write = db.writelines(userDict["Username"])
        write = db.writelines(',')
        write = db.writelines(userDict["Password"])
        write = db.writelines(',')
        write = db.writelines(userDict["Money"])
        write = db.writelines('\n')

    # Send user to roulette game to log in
    print("\n")
    print("=-" * 25)
    print("          Please log in to start playing..")
    print("-=" * 25)
    checkdetails.userlogin()