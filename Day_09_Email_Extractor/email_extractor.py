# Email Extractor

import re  # Regular Expression Module


def email_extractor(filename):
    try:
        with open(filename, "r") as file:
            text_data = file.read()

            pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


            found_emails = re.findall(pattern, text_data)
            total_count = len(found_emails)
            
            print(f"Here are the {total_count} emails found in the'{filename}': ")

            for email_address in found_emails:
                print(email_address)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

email_extractor("data.txt")

