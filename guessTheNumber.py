import math
import random
def guessNumberByComputer():
    print("Please keep the number between 0 and 100 and don't tell anybody.\nNow I will try to guess your number in 7 steps.\nLet's start...")
    number = None
    step = 7
    max = 100
    min = 0
    win = False
    while step > 0:
        number = math.floor((max+min)/2)
        print("Is the number ", number, " ?")
        answer = input("yes(y)/no(n):")
        if answer == "y":
            win = True
            break
        step = step - 1
        tip = input("up(u)/down(d) :")
        if tip == "u":
            min = number
        else:
            max = number
    if win:
        print("I won :)")
    else:
        print("You won :(")

def guessNumberByUser():
    number = random.randint(0,100)
    chance = 10
    print("I choose a number between 0 and 100. Please try to find. You have 10 chances.")
    while chance > 0:
        predict = input("Give me a number : ")
        if number == predict:
            print("You won :)")
            break
        else:
            if number > predict:
                print("Up")
            else:
                print("Down")
            chance = chance - 1

print("*****WELCOME THE GAME*****")
game_type = None
while game_type not in ["1", "2"]:
    print("1.Computer \n2.User")
    game_type = str(input("Please choose the game type : (Eg. :1,2)\n"))

if game_type == "1":
    guessNumberByComputer()

