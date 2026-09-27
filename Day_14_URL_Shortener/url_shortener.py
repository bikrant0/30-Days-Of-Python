# URL Shortener

import requests

def short_url():
    inputted_url = input("Enter the url you want to shorten.: ")
    try:
        if inputted_url.startswith("http"):
            response = requests.get(f"https://tinyurl.com/api-create.php?url={inputted_url}")

            if response.status_code == 200:
                print("Short URL: ", response.text)
            elif response.status_code == 403:
                print("The server didn't respond. ")
            else:
                print("Check your internet connection.")
                return
        else:
            print("Invalid URL. Enter a valid URL. ")
            
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check and try again.")
    
short_url()

