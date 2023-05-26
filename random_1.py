import random

highLowChosen = False

while True:
    if (highLowChosen == False):
        try:
            high = int(input("What is the highest number you would like: "))
            low = int(input("What is the lowest number you would like: "))
            num = random.randint(low, high)
            highLowChosen = True
        except:
            print("\nYOU ARE STUPID! LOWEST NUMBER CANNOT BE LARGER THAN HIGHEST NUMBER! Cope!\n\nPlease choose again :)\n")
    else:
        guess = int(input("Guess a number between {} and {}: ".format(low, high)))
        if guess == num:
            print("You guessed it right!")
            break
        elif guess > num:
            print("Too high")
        else:
            print("Too low")
