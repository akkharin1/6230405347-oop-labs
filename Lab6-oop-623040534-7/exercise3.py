def demo_readline2():
    f = open("kku.txt", "r", encoding='utf8')
    for i in range(9):
        print(f.readline())
while True:
    a = input("Enter a filename:")
    if a == "kku.txt" :
            demo_readline2()
            break
    else:
        break