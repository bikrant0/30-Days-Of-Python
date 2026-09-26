# Dictionary Saver

import json

def dictionary_saver(filename):
    try:
        with open (filename, "r") as dictionary:
            my_dictionary = json.load(dictionary)

    except FileNotFoundError:
        print("Please create a file. File is not there.")
        my_dictionary = {}

        while True:
            print("\n 1. Add a word.  2. Look up a word  3. Save and Quit. ")
            choice = int(input(" Please Enter 1,2,3 only--> "))
            
            if choice == "1":
                user_word = input("Enter the word you want to add.")
                user_def = input("Enter the definition of the word")
                my_dictionary[user_word] = user_def

                print(f"Added '{user_word}' to the dictionary. ")
                
            elif choice == "2":
                search = input("Enter the word you want to search: ")
                if search in my_dictionary['word']:
                    print(f"Definition: {my_dictionary[search]}")
                else:
                    print("Word not found.")
            

            elif choice == "3":
                with open (filename, "w") as file:
                    json.dump(my_dictionary, dictionary)
                    print("Dictionary saved successfully.")
                    break

            else: 
                print("Please enter 1,2 or 3. ")

            

         
dictionary_saver("dictonary.json")