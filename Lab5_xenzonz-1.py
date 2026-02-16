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


def main():
    print("test")
    
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    total = dice_one + dice_two

    print(f"dice one: {dice_one}")
    print(f"dice two: {dice_two}")
    print(f"total: {total}")

main()