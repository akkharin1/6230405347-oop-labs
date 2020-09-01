def check_quit(msg):
    check = str(input("Enter the first number:"))
    if check == "quit":
        return 0
    if int(check) == int:
        return int(check)

average_sum = 0
divide = 0
while True:
    integers = int(input("Enter an integers:"))
    if integers > 0:
        divide += 1
        average_sum = average_sum + integers
    elif integers < 0:
        if divide == 0:
            print("You haven't entered a positive number")
            break
        elif divide > 0:
            print(f"Average is {average_sum / divide}")
        break


