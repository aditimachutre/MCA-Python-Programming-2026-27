secret = 50

while True:

    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("Too Low")

    elif guess > secret:
        print("Too High")

    else:
        print("Correct Guess!")
        break