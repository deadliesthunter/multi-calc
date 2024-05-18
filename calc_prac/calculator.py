a = float(input("enter any 2 numbers \n"))
b = float(input("\n"))
operation = input("what operation you want to do 'sum','mul','div' \n").lower()

def switch(operation):
    if operation=="sum":
        return(f"sum = {a+b}")
    elif operation == "mul":
        return(f"mul = {a*b}")
    
    elif operation == "div":
        try:
            return(f"div = {a/b}")
        except ZeroDivisionError as err:
            print("division by zero not allowed")
print(switch(operation))        