# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Generate a random number between 1 and 1000. CHECK
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program. CHECK
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again. CHECK
#
# If the guess is too high, print "Too high!" and continue asking. CHECK
#
# If the guess is too low, print "Too low!" and continue asking. CHECK 
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts. CHECK
# ----------------------------------------------------------------------
import random
guesses = 0
is_number = False
current_guess = 0
random_number = random.randint(0, 1001)
print(random_number)
#the method to see if the user wants to quit the program or if they don't input a number
def end_program(g):
    #global keep_going
    if g == "bye" or g == "exit":
        #keep_going = False
        print("ended game.")
    else: 
        print("Please enter a valid number.")
        
        
#keeps the program repeating, the method to recieve a guess and to output if it is correct or not
print("Please type 'bye' or 'exit' to end the game.")

    #global guesses, current_guess, is_number
    
current_guess = input("What is your guess? ")
# below is to verify that the inputted value is a number
try:
     int(current_guess)
     is_number = True
except ValueError:
    is_number = False
    #if it is a number:
if is_number == True:
    if int(current_guess) == random_number:
        guesses += 1
        print("Congratulations! You guessed the number!")
        print("It took " + str(guesses) + " attempts!")
    elif int(current_guess) < random_number:
        print("That's too low, guess again.")
        guesses += 1
            
    elif int(current_guess) > random_number:
        print("That's too high, guess again.")
        guesses += 1
            
    #if it isn't a number, it runs the other method to deal with string inputs
else:
    end_program(current_guess)



#CHANGE THIS TO A WHILE LOOP TO MAKE IT BETTER