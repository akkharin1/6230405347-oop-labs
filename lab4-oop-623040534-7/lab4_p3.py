def check_quit(value):
    if value < 0 :
        quit()
    else:
        return

def divide(dividend, divisor):
    return dividend / divisor

while True :
    while True:
        try:
            dividend = int(input("Please enter the dividend:"))
            check_quit(dividend)
            break
        except ValueError :
            print("Please enter number")

    while True:
        try:
            divisor = int(input("Please enter the divisor:"))
            check_quit(divisor)
            break
        except ValueError:
            print("Please enter number")

    try:
        answer = divide(dividend, divisor)
        print('The answer is: {}'.format(answer))
    except ZeroDivisionError :
        print("Cannot perform division by zero")



