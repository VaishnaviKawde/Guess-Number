import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0

while( userGuess != randNumber):
    userGuess=int(input("enter a Number: "))
    guesses+=1
    if userGuess==randNumber:
        print("you guess it write")
    else:
        if userGuess>randNumber:
            print("you guess it wrong! Enter a smaller number")
        else:
             print("you guess it wrong! Enter a larger number")

print(f"you guess the number in {guesses} guesses")          

with open("highscore.txt",'r') as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("you just broken highscore")
    with open("highscore.txt",'w') as f:
        f.write(str(guesses))

