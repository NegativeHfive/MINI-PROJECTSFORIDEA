import random, os, time

#list coming and showing things
guessedNumber = random.randint(1,10)
lives = 10

lists = []
for i in range(10):
    lists.append(i)

try:
    while True:
        print("Guess the number")
        lists.append(guessedNumber)
        if guessedNumber == i:
            lists.remove(i)
        print(lists)
        question = int(input("Number > "))

        if lives < 0:
            print("Game Over")
            break
        else:
            if question not in lists:
                lives -= 2
                print(f"You have {lives} lives")
                print("The number should be in the list")
            elif question != guessedNumber and question in lists:
                lives -=1
                print(f"You have {lives} lives")
                print("Wrong number")
            else:
                print(f"You win the number is {guessedNumber}")
                print(f"You had {lives} lives left")
                time.sleep(2)
                break
except ValueError:
    print("Enter a number the next number")