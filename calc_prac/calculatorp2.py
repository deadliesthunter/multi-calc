import re
import math #not been use yet
def mycalculator(operations):
    
    tokens = re.findall(r'(\d+\.?\d*)|([+-/*\^])|(\w+)',operations) #token is used to separate the given expression into single unit

    result = None # used as accumulator(expression), current total
    current_operator = None # it reads the operator 

    for token in tokens :
        if token.isdigit():
            number = float(token)
            if result == None :
                result = number
            elif current_operator == "+" :
                result += number
            elif current_operator == "*" :
                result *= number
            elif current_operator == "-" :
                result -= number
            elif current_operator == "/" :
                if number != 0 : 
                    result /= number
                else:
                    print("divided by zero error :(")
                    exit()
            elif current_operator == "^" :
                result **= number
        elif token in ["+","-","*","^","/"] :
            current_operator = token
        else :
            print("invalid token : {token}")
    return result

operations = input("enter any expression \n")
print(mycalculator(operations))

