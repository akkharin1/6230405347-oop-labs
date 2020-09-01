def factorial(n):
    if n == 0 :
        return 1
    if n > 0:
        return n*factorial(n-1)

try:
    integer = int(input("Enter an integar:"))
    factorial_n = factorial(integer)

    if integer < 0:
        print("Please enter a positive integer.{} is not a positive integer".format(integer))
    elif integer > 0:
        print("factorial (%d) is %d" %(integer,factorial(integer)))
except ValueError as err:
    print("Please enter a positive integer.%s" % err)
