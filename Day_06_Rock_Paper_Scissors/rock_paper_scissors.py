# Rock Paper Scissors 

import random



 # players = input("How many players do you wanna play with? "\
  #              "--> ")
option = ("rock", "paper", "scissor")
word = ("r", "p","s")
while True:
    print("Rock, Paper, Scissor !!!")
    print("What do you Choose? R/r for Rock P/p for Paper and S/s for Scissor. ")
    user_choice = input("--> ").lower()
    if user_choice == "r":
        user_choice = "rock"
    elif user_choice == "p":
        user_choice = "paper"
    elif user_choice =="s":
        user_choice ="scissor"

    if user_choice not in option:
        print("Invalid words. Please enter valid words (Rock, Paper, Scissor or R, P, S. )")
        continue
    output = random.choice(option)
        
    if user_choice == "rock":
        print(f"Machine chose {output}, You chose Rock.")
        if user_choice == output:
            print("TIEEE !!!")
            continue
        elif output == "paper":
            print('You lose the round. Better luck next time. ')
        else:
            print('You won the round. Better luck next time. ')
                
            
    elif user_choice == "paper":
        print(f"Machine chose {output}, You chose {user_choice}.")
        if user_choice == output:
            print("TIEEE !!!")
            continue
        elif output == "rock":
            print("You won this round. Congratulations.")
        else:
            print('You lose the game. Better luck next time. ')

    elif user_choice == "scissor":
        print(f"Machine chose {output}, You chose Scissor.")
        if user_choice == output:
            print("TIEEE !!!")
            continue
        elif output == "paper":
            print("You won this round. Congratulations.")
        else:
            print('You lose the game. Better luck next time. ')           

    status = ""
    while status not in ("Y", "N", "YES", "NO"):
        status = input("\nDo you want to play another round? (Y/N): ").upper()
        if status not in ("Y", "N", "YES", "NO"):
            print("Please enter Y or N only.")
            
    if status == "N" or status == "NO":
        print("Thanks for playing! Goodbye.")
        break
        