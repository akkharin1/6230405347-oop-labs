def demo_readline2():
    with open("kku.txt", "r", encoding='utf8') as f:
        read_da = f.read()
    return read_da

y = demo_readline2()

with open("kku2.txt", "w", encoding='utf8') as outa:
    all_line = y
    outa.writelines(all_line)

    all_line = "  \nMotto: วิทยา จริยา ปัญญา\nMotto in English: Knowledge, Virtues, Wisdom"
    outa.writelines(all_line)














demo_readline2()