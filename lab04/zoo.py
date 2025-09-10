#response formula for when the user answer "help"
def show_help():
    print("You can do the following things:")
    print("Type 'help' to see this list again")
    print("Type 'see' to see all the animals")
    print("Type 'pet' followed by the animal's name to pet that animal")
    print("Type 'bye' to leave the zoo and exit the program")

#lists all the animals in the petting zoo
def show_animals():
    print("\n The animals in the zoo are:")
    print("• Clover the Bunny 🐇")
    print("• Coco the Baby Goat 🐐")
    print("• Arno the Alligator 🐊")

#petting the animal of your choice
def pet_animal(animal):
    if animal == "clover":
        print("Clover is so happy! ❤️")
    elif animal == "coco":
        print("Coco the Baby Goat thanks you! 🥰")
    elif animal == "arno":
        print("Actually, we cannot allow you to pet Arno. ⛔️")
    else:
        print("Sorry, I don't know that animal")







keep_going = True
#intro to the program
print("Welcome to the Petting Zoo!")
print("Type 'help' to get a list of all the things you can do! \n")
while keep_going:

    response = input("What would you like to do? ").strip().lower()
    if response == "help":
        show_help()
    elif response == "see":
        show_animals()
    elif response.startswith("pet "):
        animal = response[4:]
        pet_animal(animal)
    elif response == "bye":
        print("Goodbye!")
        keep_going = False
    else:
        print("Sorry, I don't know that command.")
