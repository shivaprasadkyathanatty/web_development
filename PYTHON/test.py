import random
# GET GUESS
def getGuess():
    return list(input("Guess the digits"))

 # GENERATE RANDOM digits
def rand():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

# VALIDATE GUESS
def validate():
    user_guess=getGuess()
    if user_guess==rand_digits:
        print ("Congratulations your guessed number {} matches system generated random number{}".format(str(user_guess),))
    while user_guess!=rand_digits:
        if user_guess[0] not in rand_digits and user_guess[1] not in rand_digits and user_guess[2] not in rand_digits:
            print ("NOPE")
        elif (user_guess[0] or user_guess[1]) in rand_digits[2] or (user_guess[2] or [user_guess[0]]) in rand_digits[1] or (user_guess[1] or user_guess[2]) in rand_digits[0]:
            print ("CLOSE")
        elif user_guess[0]==rand_digits[0] or user_guess[1]==rand_digits[1] or user_guess[2]==rand_digits[2]:
            print ("MATCH")
        else:




            validate()
# RUN GAME LOGIC
print ("Welcome Code Breaker! Let's see if you can guess my 3 digit number")
rand_digits=rand()
print (rand_digits)
validate()
