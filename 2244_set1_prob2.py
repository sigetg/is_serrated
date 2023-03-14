#Author: George Sigety

import random

#function that determines if a set of five rolls is serrated
def is_serrated(five_rolls):
    if five_rolls[1] > five_rolls[0]:
        if five_rolls[2] < five_rolls[1]:
            if five_rolls[3] > five_rolls[2]:
                if five_rolls[4] < five_rolls[3]:
                    return True
    if five_rolls[1] < five_rolls[0]:
       if five_rolls[2] > five_rolls[1]:
            if five_rolls[3] < five_rolls[2]:
                if five_rolls[4] > five_rolls[3]:
                    return True
    return False

# Sample space is 6 sides of a die:
sample_space = [1, 2,  3, 4, 5, 6]
#set the arrays to hold the 10^6 sequences of 5 die rolls and each set of 5 rolls
five_roll = [0,0,0,0,0]
rolls = [None] * 10**6
i = 0
no_serrated = 0
#fill the array with 10^6 sequences of 5 random die rolls
while i < 10**6:
    x = 0
    while x < 5:
        five_roll[x] = random.choice(sample_space)
        x += 1
    #count the number of 5 rolls that are serrated
    if (is_serrated(five_roll)):
        no_serrated += 1
    five_roll = [0,0,0,0,0]
    i += 1

# solve for the probability using |E|/|S|
probability_serrated = no_serrated / 10**6

#print the probability
print(probability_serrated)
