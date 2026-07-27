"""
WorkFlow of project
1- Input from user(Rock, Paper< Scissor)
2- Computer Choice (will choose randomly)
3- result print

Cases:
A- Rock:
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B- Paper:
Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor:
Scissor - Scissor = Tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor =").capitalize()

# Valid data input
if user_choice not in item_list:
    print("Invalid Choice! Please enter Rock, Paper, Scissor.")
    exit()
    
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rocks = Computer win")
    else:
        print("Rock smashes Scissor = You win")    

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Computer cut paper = Computer win")
    else:
        print("Paper cover rock = You win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cut paper = You win") 
    else:
        print("Rock smashes scissor = Computer win")   
