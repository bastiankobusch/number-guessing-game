import random

def spiel ():
    print("Welcome to: Guess the number!")
    print()
    print("I have picked a random number between (1-10) for you to guess.\n\n")

    # Bot chooses random number
    number = random.randint(1, 10)

    Try_count = 3 #Setting for amount of tries

    #Gameloop
    while Try_count > 0:
        try:
            user_input = int(input("Your guess between (1-10) "))

        #Checking user_input
            if user_input  < 1 or user_input > 10:
                print ("Please input numbers from (1-10) only!\n\n")
                continue

        except ValueError:
            print("It appears that wasnt a valid number, try again.\n\n")

        #Game logic
        if user_input == number:
            print("\nCongratulations, you won!")
            return
        else: 
            Try_count -= 1

            if user_input < number:
                print("\n\nToo low.\n\n\n")

            else:
                print ("\n\nToo high.\n\n\n")
 
            print (f"Remaining guesses: {Try_count}\n\n")        

    #If try_count is 0 (Game lost)
    print(f"Unfortunately you lost, the number was {number}.")

#Starting the game
spiel()
input("\n\n\nGame over. Press Enter to close.")
