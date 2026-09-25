# Weather App

import json

def weather_app(filename):
    try: 
        # Opening json file
        with open(filename, "r" ) as file:
            data = json.load(file)
    except FileNotFoundError:
            print("File not found.")
            return

        
    
    cityn= input("Enter the city name that you want to see weather of ? ")
    found = False
    for item in data:
        if item["city_name"] == cityn:
            found = True
            print(f"The weather in {item['city_name']} is like this: \n"
                  "---------------------------- \n"
                  f"Temperature: {item['main']['temp']} K \n"
                  f"Clouds: {item['clouds']}%\n"
                  f"Date: {item['dt_iso']}")
            break
        
        if found == False:
            print("Enter a valid location.")
                
    
    

weather_app("history_bulk.json")

            
