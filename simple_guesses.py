#!/usr/bin/env python3

"""
The goal of this script is to create a back and forth between two players.
Player1 will pick a number between 1 and 10, player 2 will try to guess it,
with player 1 saying "guess is too high or low" in response to the guess.
"""

import random

# in this setup, the range of numbers is [0,10) and since the learning rate is 1 step
# it will take at most 10 operations (number_of_guesses)

### Next ToDo:
### * find the simplest improvement to the update_guess 
### * wrap in a simulation function that returns how many guesses it took
### * add more distinguishing features to both players, then create classes


def single_increment():
    # player1_numbers
    random_number1 = int(random.random()*10)
    random_number2 = int(random.random()*10)
    
    number_of_guesses = 0
    got_it = False
    while not got_it:
        number_of_guesses += 1
        if random_number2 > random_number1:
            print("guess is too high")
            random_number2 = update_guess_single_step(random_number2, -1)
            continue
        if random_number2 < random_number1:
            print("guess it too low")
            random_number2 = update_guess_single_step(random_number2, +1)
            continue
        if random_number2 == random_number1:
            print("guess is correct!")
            got_it = True
            print("took %s guesses" % number_of_guesses)

def update_guess_single_step(guess, gradient):
    learning_rate = 1
    if gradient == -1:
        return guess - learning_rate
    if gradient == +1:
        return guess + learning_rate

