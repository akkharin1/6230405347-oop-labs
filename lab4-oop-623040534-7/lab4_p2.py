def check_quit(num):
    cheque = input(num)
    if cheque == "quit":
        return 0
    elif cheque != "quit":
        try:
            cheque = float(cheque)
        except ValueError :
            print("Please enter a number")
            return check_quit(num)
        else:
            return cheque
        print("Enter number or \"quit\" word to  end program")

while True:
    first_number = check_quit("Please enter the first operand:")
    second_number = check_quit("Please enter the second operand:")
    operator = str(input("Please enter the operator"))
    if operator == "+":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    elif operator == "-":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operator == "*":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    elif operator == "/":
        if  second_number == 0:
            print("Cannot divide  by zero")
        else:
            print(f"{first_number} / {second_number} = {first_number / second_number}")
    elif operator == "quit":
        break
    else:
        print("Unknow operator")
