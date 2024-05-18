


take = input('''which calculator do u want to use
             1: 2 input taker
             2: single input taker ''')

match take:             #using switch case where match and case is used
    case "1":
        from calculator import switch
    case "2":
        from calculatorp2 import mycalculator
    case _:
        print("sorry no other calculator is present. Have a nice day")

