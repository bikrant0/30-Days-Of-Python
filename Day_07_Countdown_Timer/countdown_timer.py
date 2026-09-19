# Countdown Timer

import time

while True:
    while True:
        try:
            minutes = int(input("How many minutes do you want for the timer? --> "))
            if minutes <= 0:
                print("Please eneter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number(no letters)")

    total_seconds = minutes * 60
    print("\n Timer has Started...")


    while total_seconds > 0:
        print(f"Time remaining: {total_seconds} seconds...")
        time.sleep(1)
        total_seconds -= 1

    print("\n Time's up! Your timer has ended. \n")

    opt = input ("Do you want tot run the timer again? (Y/N)").upper()
    if opt == "N" or opt == "NO":
        print("Thanks for using the timer. Goodbye!")
        break