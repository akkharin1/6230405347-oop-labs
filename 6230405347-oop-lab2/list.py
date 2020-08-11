list_weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
list_weekend = ['Saturday', 'Sunday']

print("Weekday are %s " % list_weekday)
for i in list_weekend:
    list_weekday.append(i)
print("Weekend are %s " % list_weekend)
print("Days are %s " % list_weekday)
print("Sorted days are %s" % sorted(list_weekday))
print("Reversed days are %s" % list(reversed(list_weekday)))
print("The last two days of list days are %s " % (list_weekday[5:]))



