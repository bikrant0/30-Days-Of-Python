# Mad Libs Generator

import random
keep_playing = "Y"
prompts = ["day", "noun", "adj", "adj1", "adj2", "adj3"]
answers = {}
adj, adj1, adj2, adj3 = ""
def mad_libs():
    journal = "Today i woke up and it was {day}. I was {adj} about the {noun} and {verb}. I planned to do something {adj2} and might {adj3} anybody, " \
            "do it together with {noun1} and have {adj4}. Here is what I {adj2} to do but something came up. I end up doing {adj3}. Well, it was really great day."

valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
random_adj = ["fluffy","grumpy","great","fabulous","sparkly", "gigantic"]
random_verbs = ["dance","jump","sleep", "sing", "run"]

    
while keep_playing == "Y":
    for prompt in prompts:
        day = input("Enter any Days ").lower()
        noun = input("Enter the noun words: ").lower()
        adj = input("Enter the adjective word or for random words(Type s/S): ").lower()
        adj1 = input("Enter any adjective word or for random words(Type s/S): ").lower()
        adj2 = input("Enter any adjective word or for random words(Type s/S): ").lower()
        adj3 = input("Enter any adjective word or for random words(Type s/S): ").lower()
        verb = input("Enter any verb words or for random words(Type s/S): ").lower()
        while len(adj) < 2:
            adj = input ("Enter an adjective (1 or 2 words only): ")

            if len(adj.split()) > 2:
                print("To many words! Try Again.")
        
        if day not in valid_days:
            print("Please enter a valid name of day.")
        else:
            break

        answers[prompt] = day
        answers[prompt] = noun
        answers[]

        
        mad_libs()

    keep_playing = input("Do you want to play another round? (Type Y/N): ").upper()
    if keep_playing == "N":
        break
