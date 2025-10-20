import random
def guess_number():
    targest_number=random.randint(1,9)
    while True:
        user_guess=int(input("gues a number between land9:"))
        if user_guess==targest_number:
            print("well guessed!")
            break
        else:
            print("wrong guess. try again")
guess_number()
