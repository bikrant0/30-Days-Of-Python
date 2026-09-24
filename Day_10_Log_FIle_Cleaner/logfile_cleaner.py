# Log File Cleaner

import re

def log_file_cleaner(filename):
    try:
        pattern = r"\[DEBUG\]"
        clean_filename = "clean_log.txt"

        # Opening the messy file for reading.
        with open(filename, "r") as messy_file:

            # Opening new file for writing:
            with open(clean_filename, "w") as clean_file:

                for line in messy_file:
                    if not re.search(pattern, line):
                        clean_file.write(line)

            print(f"Cleaning complete! Created {clean_filename}.")

 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
         

    
log_file_cleaner("log.txt")