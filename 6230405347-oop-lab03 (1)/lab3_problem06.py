month = ("January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December")
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
dict_day_month = {}
for i in range(0, 12):
      dict_day_month[month[i]] = days[i]
month_insert = input("Enter month:")
print(f"Number of days in {month_insert} is {dict_day_month[month_insert]}")