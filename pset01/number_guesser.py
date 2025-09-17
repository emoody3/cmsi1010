#Programmer: Estella Moody CMSI1010 section 3
import random
guesses = 0
is_number = False
current_guess = 0
random_number = random.randint(0, 1001)
#print(random_number) - I used this to help me test code before I fully finished it. 
go = True
#the method to see if the user wants to quit the program or if they don't input a number

def end_program(g):
    global go
    if g.lower() == "bye" or g.lower() == "exit":
        print("ended game.")
        go = False
    else: 
        print("Please enter a valid number.")
        run_program()
        

#start of game that takes a number
print("Please type 'bye' or 'exit' to end the game.")
def run_program():
    global guesses, current_guess, is_number, random_number, go
    while go:
        current_guess = input("What is your guess? ")
        # below is to verify that the inputted value is a number
        try:
            int(current_guess)
            is_number = True
        except ValueError:
            is_number = False
        #after verifying that the guess was a number, see if it is too big, small, or correct
        if is_number == True:
            if int(current_guess) == random_number:
                go = False
                guesses += 1
                print("Congratulations! You guessed the number!")
                print("It took " + str(guesses) + " attempts!")
            elif int(current_guess) < random_number:
                print("That's too low, guess again.")
                guesses += 1
                    
            elif int(current_guess) > random_number:
                print("That's too high, guess again.")
                guesses += 1
                    
            #if it isn't a number, it runs the other method to deal with string inputs or the exit/bye command
        else:
            end_program(current_guess)


#run the program
run_program()