"""
Docstring for Lab5_xenzonz_1
i. LAB 5: Dice Rolling Terms
ii. Sam Cocquyt
iii. Program that rolls two dice, prints the outcome, and then uses conditional statements to print the appropriate term for that roll.
    Repeats until the user quits
iv. No starter code
v. 2/15/2026
"""

import random

def get_dice_term(dice_one, dice_two):
    #total = dice_one + dice_two

    #print(total) #test

    if dice_one == 1 and dice_two == 1: 
        return "Snake Eyes"
    elif (dice_one == 2 and dice_two == 1) or (dice_one == 1 and dice_two == 2):
        return "Ace Caught a Deuce"
    elif dice_one == 2 and dice_two == 2:
        return "Little Joe from Kokomo"
    elif (dice_one == 3 and dice_two == 2) or (dice_one == 2 and dice_two == 3) or (dice_one == 4 and dice_two == 1) or (dice_one == 1 and dice_two == 4):
        return "Little Phoebe"
    elif dice_one == 3 and dice_two == 3:
        return "Jimmy Hicks from the Sticks"
    elif (dice_one == 6 and dice_two == 1) or (dice_one == 1 and dice_two == 6):
        return "Six Ace"
    elif dice_one == 4 and dice_two == 4:
        return "Eighter from Decatur"
    elif (dice_one == 3 and dice_two == 6) or (dice_one == 6 and dice_two == 3) or (dice_one == 4 and dice_two == 5) or (dice_one == 5 and dice_two == 4):
        return "Nina from Pasadena"
    elif dice_one == 5 and dice_two == 5:
        return "Puppy Paws"
    elif (dice_one == 6 and dice_two == 5) or (dice_one == 5 and dice_two == 6):
        return "Six Five no Jive"
    elif dice_one == 6 and dice_two == 6:
        return "Boxcars"
    else:
        return "No special term for this combination of dice"

    



def main():
    print("test123")
    
    while True:
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        total = dice_one + dice_two

        print(f"Dice One: {dice_one}")
        print(f"Dice Two: {dice_two}")
        print(f"Dice Total: {total}")

        term = get_dice_term(dice_one, dice_two) 
        print(term) 

        user_choice = input("test tpye q")
        if user_choice == "q":
            break


main()
