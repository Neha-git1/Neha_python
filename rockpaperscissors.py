import random

print("ROCK PAPER SCISSORS GAME")
number = int(input("How many rounds do you want to play? "))
score = 0
choice=['rock','paper','scissors']
for i in range(number):
    userchoice=input("enter your choice ")
    if userchoice not in choice:
        print("invalid input")
        continue
    computerchoice = random.choice(choice)
    print(f"computer chose {computerchoice}")
    if computerchoice==userchoice:
        print("TIE")
    elif (computerchoice=='rock' and userchoice=='scissors') or (computerchoice=='paper' and userchoice=='rock') or (computerchoice=='scissors' and userchoice=='paper'):
        print("YOU WON")
        score+=1
    else:
        print("YOU LOST")
        score+-1
print("thanks for playing, your score is ",score)
