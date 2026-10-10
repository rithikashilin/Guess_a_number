#guess a random number between 1-100

import random
number=random.randint(1,100)

while True:
    guess=int(input("guess a number between 1 to 100 : "))
    if guess== number:
        print("Correct Guess")
        break
    elif guess<number:
        print("Too Low")
    else:
        print("To High")
