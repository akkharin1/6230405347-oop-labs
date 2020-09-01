import sys

def robust_calculator():
    while True:
        first_number = float(first_number)
        second_number = float(second_number)
        operator == ("+", "-", "*", "/")
        if operator is None:
            continue
        requested_format = ("+", "-", "*", "/")
        output = calculator(first_number, second_number, operator, requested_format)
        if output is not  None:
            if operator == "":
                operator = ADD

            print("{} {} {} = {}".format((first_number, second_number, op2, output)))
        else:
            print("we cannot")

def check_quit(msg):
    while True:
        cheque = input(msg)
        if cheque == "q" or cheque == "Q" :
              sys.exit()
        elif cheque != "q":
            try:
                cheque = float(cheque)
            except ValueError:
                print("Please enter a number")
            else:
                return cheque



while True:
    while True:
        first_number = check_quit("Please enter the first operand ('q' to quit):")
        break
    second_number = check_quit("Please enter the second operand :")
    operator = str(input("Enter an operation('+', '-', '*', '/'):"))
    output_format = input("Enter output format (float, int)")


    if operator == "+" or operator == '':
        if output_format == "int":
            sum = round(first_number + second_number)
        elif output_format == "float" or output_format == " ":
            sum = float(first_number + second_number)
        print(f"{first_number} + {second_number} = {sum}")
    elif operator == "-" or operator == '':
        if output_format == "int":
            sum = round(first_number - second_number)
        elif output_format == "float" or output_format == " ":
            sum = float(first_number - second_number)
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operator == "*":
        if output_format == "int":
            sum = round(first_number * second_number)
        elif output_format == "float" or output_format == " ":
            sum = float(first_number * second_number)
        print(f"{first_number} * {second_number} = {sum}")
    elif operator == "/":
        if first_number == 0 or second_number == 0:
            print("Cannot divide a number by zero")
            print("we cannot perform your requesed calculation")
        else:
            if output_format == "int":
                sum = round(first_number / second_number)
            elif output_format == "float" or output_format == "":
                sum = float(first_number / second_number)
            print(f"{first_number} / {second_number} = {first_number / second_number}")
    elif operator == "q":
        break
    else:
        print("Operation must be ADD, SUB, MUL or DIV")

