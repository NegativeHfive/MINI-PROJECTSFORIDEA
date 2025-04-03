#importing random
import random, os, sys,time

guessedNumber =random.randint(1,10)
lives = 10

while True:
    print("Guess the number")
    question = int(input("Enter the number > "))
    
    if lives < 0:
        print("Game Over")
        break
    else:
        if question != guessedNumber:
            lives -= 2
            print(f"You have lost some attempts. You have {lives} left")
            time.sleep(1)
            
        else:
            print(f"You win the number is {guessedNumber}")
            time.sleep(2)
            break