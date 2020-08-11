temperature_f = False
while not temperature_f:
    try:
        temperature_f = float(input("Enter a temperature in Fahrenheit: "))
        temperature_c = (5/9) * (temperature_f - 32)
    except ValueError:
        print("Please enter a valid floating point for the temperature.")
    else:
        print("Temperature %.2f"%temperature_f, "in Fahrenheit is %.2f"%temperature_c, "in Celsius")
