import random
randomno=random.randint(1,100)
userGuess=None
guesses=0

while(userGuess!=randomno):


    userGuess=int(input("Enter your Guess: "))
    guesses+=1
    if(userGuess==randomno):
       print("Your Guess was correct!!")
   
    else:
        if(userGuess>randomno):
            print("*************You guuessed wrong guess a lower number*****************")
        else:
            print("You guessed it wrong go higher")
print(f"You guessed the number in {guesses} guesses")
with open("guesshighscore.txt",'r') as f:
    guesshighscore=int(f.read())
if(guesses<guesshighscore):
    with open("guesshighscore.txt",'w') as f:
        f.write(str(guesses))
        print(f"New high score is {guesses}")

else:
    print("Not high sore")

