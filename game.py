# this program demonstrates a guessing
# game
from random import randint

# 1 get user input
username = input("what's your name? ")
print("Hello there " + username + "!")

# 2 generate a random number
random_number= randint(10,50)

# 3 using a while loop.
# check if user input is equal for generated number
counter=0
while counter < 5:


    user_number = eval(input("enter a number:"))

    counter +=1

    if user_number < random_number:
        print("your guess is to low")
    elif user_number > random_number:
        print("your guess is too high")
    elif user_number == random_number:
        print("you win")
        break
        print("game over:")
    if user_number == random_number:
        print("you win")
    else:
         print("game over! The correct ansewer is!")
         print(random_number)

    

