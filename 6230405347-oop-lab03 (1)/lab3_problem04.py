n = int(input("Enter a number to find the factorial :"))
fac_store = n
factorial = 1
while True:
    factorial = n * factorial
    n -= 1
    if n == 1:
        print(f"Factorial of {fac_store} is {factorial}")
        break