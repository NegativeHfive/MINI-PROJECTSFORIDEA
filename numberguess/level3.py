import random, os , time

"""
Things the game should have
- A list from 1 - 100
- if geussedNumber is closer to the actual number you get some life 
- if its far you lose some life 
so for example if the actual number is 10 and you input 9,8,7,11 or 12, 
If your lives are
10? you will get 10.5 however if the number is far lets say 5, 3, 2 or 20 
you will loose amount of lives could move from 10 to 8 if its extreme then 
could be 6 or 9. 

"""

lives = 10

lists = []

for i in range(100):
    lists.append(i)

selectedItem = random.sample(lists,10) # picks a few items from the lists
random.shuffle(selectedItem)

guessedNumber = random.choice(selectedItem)


try:
    while True:
        print("GUESS THE NUMBER")
        print(selectedItem)
        print()
        question = int(input("Enter the number > "))
        

        if question not in selectedItem:
            lives -= 4
            if lives <= 0:  # Check after deduction
                print("Game Over")
                break
            print("Please choose the number from the lists")
            print(f"You have {lives} lives left")

        elif question != guessedNumber and 2 < question < 3 :
            lives += 0.5
            print("You are close almost there. You are close")
            print(f"You have {lives} lives left")
        
        elif question != guessedNumber and 5 < question > 3 :
            lives -= 3
            print("It's far from the actual number")
            print(f"You have {lives} lives left") 
            if lives <= 0:  # Check after deduction
                print("Game Over")
                break
        else:
            print(f"You win the number is {guessedNumber}")
            print(f"You had {lives} lives left")
            time.sleep(2)
            break
except ValueError: 
    print("Enter a number the next number")
    pass