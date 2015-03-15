num=10
to_guess=True
while to_guess:
    guess=int(input("guess the num:"))
    if guess==num:
        print("u guessed it right!")
        to_guess=False
    elif guess<num:
        print("ur guess is lesser than secret no.")
    else:
        print("ur guess is larger than secret no.")
