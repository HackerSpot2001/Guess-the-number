from random import randint
from math import log

lowerValue = int(input("Enter Lower value: "))
upperValue = int(input("Enter Upper value: "))
value = randint(lowerValue,upperValue)
print("\nYou've only: ",round(log(upperValue - lowerValue + 1, 2))," chances to guess the integer!\n")

count = 0
while count < log(upperValue-lowerValue+1,2):
    count+=1
    guess = int(input("Guess a number:- "))
    if value == guess:
        print("Congratulations you did it in ",count, " try")
        break
    elif value > guess:
        print("You guessed too small!")
    elif value < guess:
        print("You Guessed too high!")
    
    if count >= log(upperValue - lowerValue + 1, 2):
        print("\nThe number is %d" % value)
        print("\tBetter Luck Next time!")