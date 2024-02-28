# guessing game
from random import randint
import sys

# game level variabel is used to keep track of levels i..e., easy or hard
game_level = input("Enter the level you want to play 'e' for easy or 'h' for hard!: ").lower()

# logic to assign the no of life avilabel to player
if game_level == "e":
    life = 10
elif game_level =="h":
    life = 5
else:
    sys.exit("Please provide valid based on above information")



# randint is function which returns random number within specified range
answer = randint(1,11)
while life >0:
    print(f"no of chances left: {life}")
    # variabel which stores user choice number
    gamer_choice = int(input("Guess the number between 1 and 10: "))
    if gamer_choice == answer:
        print("You Won!!!!!")
        break
    else:
        life -=1
if life <=0:
    print("Oops! you ran out of your luck,you loose ")
    print(f"actual answer is {answer}")






# life variabel is used to keep track of no of chances avilabel for gamer
