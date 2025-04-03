import random , os, sys
# Making a risks game just for the console

#first one
chosenNumber = random.randint(1,10)
attempts = 10
while attempts:
    answer = int(input("Enter number > "))
    print("Guess the number")
    print()
    if answer == chosenNumber :
        print(f"correct the number is {chosenNumber}. You win")
        break
    elif answer != chosenNumber:
        print("number is wrong")
        attempts -= 1

    if attempts < 0: 
        print("Game Over")

# code above is not good enough could be better and great but not the best 



