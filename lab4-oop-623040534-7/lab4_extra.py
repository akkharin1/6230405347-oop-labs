list_num = input("Enter the list of numbers(delimited by a comma):").split(",")
print(num)
try :
    index = int(input("Enter an dex:"))
    print(list_num[index])
except IndexError :
    print("The list has no element at index %d."% index)