"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

import random

NUM_SIDES = 6          # constant: sides on each die (global scope)


def roll_dice():
    """Roll two dice once and print the individual results plus the total."""
    # ----- local scope inside function -----
    die1 = random.randint(1, NUM_SIDES)   # local variable
    die2 = random.randint(1, NUM_SIDES)   # local variable
    total = die1 + die2                   # local variable
    print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")


def main():
    """Drive the simulation, showing how a local variable is unaffected."""
    die1 = 10   # local to main(); unrelated to die1 in roll_dice()
    print(f"die1 in main() starts as: {die1}\n")

    for _ in range(3):      # roll the dice three times
        roll_dice()

    print(f"\ndie1 in main() is still: {die1}")  # unchanged


if __name__ == '__main__':
    main()