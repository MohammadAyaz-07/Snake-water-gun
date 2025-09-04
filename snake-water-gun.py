import random

# computer input
computer = random.choice([1,-1,0])

# user input
youstr = input("Enter your choice (snake/water/gun): ").lower()
# dictionaries
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

# printing values
print(f"Your choice: {reverseDict[you]}\nComputer choice: {reverseDict[computer]}")

# conditions / rules

if(computer == you):
    print("It is tie")

else:
    if(computer == 1 and you == -1) or (computer == 0 and you == 1) or (computer == -1 and you == 0):
        print("You Lose!")

    else:
        print("You win!")