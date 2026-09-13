print("Welcome to The Basic Calculator")
status = "Y"
def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")

def sub(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")

def mult(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")

def div(a,b):
    print(f"Division of {a} and {b} is {a/b}")

while status == "Y":
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    opt = input("What do you want to do? (+, -, *, /) ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
            print("Please enter a valid number. Please try again.")
    if opt == "add" or opt =="+":
        add(a,b)
    elif opt == "sub" or opt =="-":
        sub(a,b)
    elif opt == "mult" or opt =="*":
        mult(a,b)
    elif opt == "div" or opt =="/":
        div(a,b)       
    

    status = input("Do you want to continue doing calculations? (Y or N)").upper()
    if status == "N":
        break


        




    



