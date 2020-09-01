month = ("January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_insert = input("Enter month:")
zip_dict = dict(zip(month, days))
print(f"Number of days in {month_insert} is {zip_dict[month_insert]}")

