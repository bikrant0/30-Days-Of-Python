# Number GUessing Game

import random
keep_playing = "Y"

print("Welcome To The Number Guessing Game!!!!")
user_ready = input("Are you ready to play the game ?! YES or NO Type Y/y or N/n.").upper()


while keep_playing == "Y":     
        num_spec = int(input("Specify the range of number you want to guess.  1 - ?? "))


        n = random.randint(1,num_spec)
        print(f"The number is between 1 to {num_spec}")
        guess = int(input("Guess the number."))

        while n != guess:
            print(f"Your guess is not correct. Better luck next time.")
            guess = int(input("Try again.  "))

        print("You have successfully guess the number. I think you are Genius than me.")
        keep_playing = input("Do you want to play again?? Type Y or N: ").upper()


        if keep_playing == "N":
              break
        print("Thanks for playing.")
    

    
    


