"""This code prompts the user for their first and last name as well as their age\
if they are a US citizen and then asks for the state and zipcode they live in\
to print out their info for a voter registration ballot and time until they receive."""

# Asks user if they are here for the voter ballot
ballotLoop = input("Hey there, are you here for the voter ballot? Exit to stop.\n")
# Begins while loop
while ballotLoop != "exit":
    # Variable to store last name and asks user for last name
    lastName = input("Please enter your last name.\n")
    # Variable to store first name and asks user for first name
    firstName = input("Please enter your first name.\n")
    # Variable to store age and asks user for age
    age = int(input("Please enter your age.\n"))
    # Variable to ask user yes or no, if a US citizen
    usCit = input("Are you a United States Citizen?\n")
    # If the user is a US citizen and age is appropriate between 18 - 80, prints following
    if usCit == "yes":
        if 18 <= age < 80:
            print(firstName, lastName + ". Is over 18, a US citizen and may complete this form\n")
            # Variable to store state, asks what state user lives in
            state = input("What state do you currently reside in?\n")
            # Variable to store zipcode and asks user for zipcode
            zipcode = input("What is your current zipcode\n")
            # Prints all the data
            print("Alright so to make sure everything is correct we have the following.\n"
                  + firstName, lastName + ", you are " + str(age) + " years old.\n\
              You marked " + usCit + " for being a US citizen.\n\
              You currently reside in " + state + " and your zipcode is " + zipcode + "\n")
            # If state starts with a, b, c, ballot will take 1 week to receive
            if state[0] == "a" or state[0] == "b" or state[0] == "c":
                print("You should receive your ballot in 1 week\n")
            # If state starts with d, f, g, ballot will take 4 week to receive
            elif state[0] == "d" or state[0] == "f" or state[0] == "g":
                print("You should receive your ballot in 4 weeks\n")
            # If state starts with m, l, t, ballot will take 2 week to receive
            elif state[0] == "m" or state[0] == "l" or state[0] == "t":
                print("You should receive your ballot in 2 weeks\n")
        # If age is less than 18 user can not proceed
        elif 0 < age < 18:
            print("I am sorry you are not old enough to complete this voter form.")
            ballotLoop = input("I'm going to need you to exit the program.\n")
            if ballotLoop == "exit":
                print("As well as exit the ballot prompter.Come back when you are a little older!")
        # If age is over 99, prints error because age is not appropriate
        elif age > 99:
            print("Error age does not make sense.\n")
        # If age is less than -1, prints error because age doesn't make sense
        elif age < -1:
            print("Error age does not make sense.\n")
    # If user is not a US citizen, stops the process and tells the user they can't complete
    elif usCit == "no":
        print("I am sorry but you may not complete this form,\
 I am going to have to ask you to leave.")
    # Print statement to see if user would like to fill out another form and continue loop
    ballotLoop = input("Would you like to fill out another ballot? Exit to stop.\n")
    # If user enters exit, ends loop and prints following end statement
    if ballotLoop == "exit":
        print("Thank you for your vote today, every little bit makes a difference!!")
