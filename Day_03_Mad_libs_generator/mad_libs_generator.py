# Mad Libs Generator

import random
keep_playing = "Y"
prompts = ["day", "noun", "adj", "adj1", "adj2", "adj3", "verb"]
answers = {}

     
valid_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
random_noun = ["ram", "hari", "john", "Stephine"]
random_adj = ["fluffy","grumpy","great","fabulous","sparkly", "gigantic"]
random_verbs = ["dance","jump","sleep", "sing", "run"]

while keep_playing == "Y":
    for prompt in prompts:
        if prompt == "day":
            answers["day"] = input("Enter the day or for random days(Type s/S): ").lower()

            while answers["day"] not in valid_days and answers["day"] != "s":
                answers["day"] = input("Enter the day (or 's' for random): ").lower()
                

            if answers["day"] == "s":
                answers["day"] = random.choice(valid_days)

        elif prompt == "noun":
            answers["noun"] = input("Enter the noun word or for random words(Type s/S): ").lower()            
            while len(answers["noun"]) < 3 and answers["noun"] != "s":
                answers["noun"] = input("Enter a valid noun (or 's' for random): ").lower()
                            
            if answers["noun"] == "s":
                answers["noun"] = random.choice(random_noun)

        elif prompt == "adj":
            answers["adj"] = input("Enter the adjective word or for random words(Type s/S): ").lower()
            
            while len(answers["adj"]) < 3 and answers["adj"] != "s":
                answers["adj"] = input("Please enter valid adjective (or 's' for random): ").lower()
                            
            if answers["adj"] == "s":
                answers["adj"] = random.choice(random_adj)

        elif prompt == "adj1":
            answers["adj1"] = input("Enter the adjective word or for random words(Type s/S): ").lower()
            while len(answers["adj1"]) < 3 and answers["adj1"] != "s":
                answers["adj1"] = input("Please enter valid adjective (or 's' for random): ").lower()
                            
            if answers["adj1"] == "s":
                answers["adj1"] = random.choice(random_adj)

        elif prompt == "adj2":
            answers["adj2"] = input("Enter the adjective word or for random words(Type s/S): ").lower()
            while len(answers["adj2"]) < 3 and answers["adj2"] != "s":
                answers["adj2"] = input("Please enter valid adjective(or 's' for random): ").lower()
                            
            if answers["adj2"] == "s":
                answers["adj2"] = random.choice(random_adj)

        elif prompt == "adj3":
            answers["adj3"] = input("Enter the adjective word or for random words(Type s/S): ").lower()
            while len(answers["adj3"]) < 3 and answers["adj3"] != "s":
                answers["adj3"] = input("Please enter valid adjective(or 's' for random): ").lower()
                            
            if answers["adj3"] == "s":
                answers["adj3"] = random.choice(random_adj)

        elif prompt == "verb":
            answers["verb"] = input("Enter any verb or for random words(Type s/S): ").lower()
            while len(answers["verb"]) < 3 and answers["verb"] != "s":
                answers["verb"] = input("Please enter valid verb (or 's' for random): ").lower()
                            
            if answers["verb"] == "s":
                answers["verb"] = random.choice(random_verbs)


    print(f'Today i woke up and it was {answers["day"]}. I was {answers["adj"]} about the {answers["noun"]} and {answers["verb"]}. I planned to do something {answers["adj1"]} and might {answers["adj2"]} anybody, do it together with {answers["noun"]} and have {answers["adj1"]} . Here is what I {answers["adj2"]} to do but something came up. I end up doing {answers["adj3"]}. Well, it was really great day.')

    keep_playing = input("Do you want to play another round? (Type Y/N): ").upper()
    if keep_playing == "N":
            break