import checkdetails
import getdetails

# This is the main function
def start():

    # Get user input to redirect user to modules with exception handling
    global userInput
    try:
        userInput = int(input("\nSign in  |  1\n"
                              "Log in   |  2 :"))

    except ValueError:
        print("You can only enter numbers!\n")
        start()

        # If user wants to register
    if userInput == 1:
        print("\n")
        print("=-" * 25)
        print("                  Signing up..")
        print("-=" * 25)
        getdetails.userregister()

        # If user want to log in
    elif userInput == 2:
        print("\n")
        print("=-" * 25)
        print("                  Logging in..")
        print("-=" * 25)
        checkdetails.userlogin()

        # If user enters something else than 1 or 2
    else:
        print("An error has occured, please try again!\n")
        return start()



start()