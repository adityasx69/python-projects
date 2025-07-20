# Snake Water Gun Game

'''
Rules: 
    Snake > Water
    Water > Gun
    Gun > Snake
'''

import random

computer = random.choice([1,-1,0])
print("Enter 's' for snake, 'w' for water or 'g' for gun")
youInp = input("Enter your input: ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youInp]

print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(you == computer):
    print("It's a draw")


else:
    if(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You win!")
    else:
        print("Something went wrong")