# Tip  Calculator

status = "Y"
totaltip = 0.0

print(' Welcome to Tip Calculator. "Where every tip counts. " ')
print(" Feel Free To Tip Us. ")
while status == "Y": 
    
    while True:
        tip = input("Please enter the amount you want to TIP? ")
        try:
            totalamount = float(tip)
            break
        except ValueError:
            print("That's not a valid number! ")
            continue

    totaltip = round(totaltip,2) + round(totalamount,2)
    print(f"You have tipped ${totalamount} abd total tip you gave is ${round(totaltip,2)}.")    

    status = input("Do you want to TIP again. Type Y/N. ").upper()

print("Thanks for Tippping. Please come again!")
