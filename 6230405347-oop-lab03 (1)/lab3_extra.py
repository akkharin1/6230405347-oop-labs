def lab3_special():
    while True:
        try:
            first_number = check_quit("Enter the first number:")
            second_number = check_quit("Enter the second number:")
            operator = str(input("Enter the operator"))
        except ValueError:
            break
        if operator == "+":
            print(f"{first_number} + {second_number} = {first_number + second_number}")
        elif operator == "-":
            print(f"{first_number} - {second_number} = {first_number - second_number}")
        elif operator == "*":
            print(f"{first_number} * {second_number} = {first_number * second_number}")
        elif operator == "/":
            if first_number == 0 or second_number == 0:
                print("Cannot divide a number by 0")
            else:
                print(f"{first_number} / {second_number} = {first_number / second_number}")
        elif operator == "quit":
            break
        else:
            print("Unknow operator")
    return

if _name_ == '_main_':
    while True:
        n = int(input("Select problem 1 - 11, print 0 is end:"))
        if n > 11 or n < 0:
            print("Select problem again!!")
        if n != 0 and n < 12:
            print(f">>> now running lab03 problem {n} <<<")
        if n == 1:
            lab3_p1()
        if n == 2:
            lab3_p2()
        if n == 3:
            lab3_p3()
        if n == 4:
            lab3_p4()
        if n == 5:
            lab3_p5()
        if n == 6:
            lab3_p6()
        if n == 7:
            lab3_p7()
        if n == 8:
            lab3_p8()
        if n == 9:
            lab3_p9()
        if n == 10:
            lab3_p10()
        if n == 11:
            lab3_special()
        if n == 0:
            break