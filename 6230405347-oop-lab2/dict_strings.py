string ={"manee": "1234", "mana": "4567", "chujai": "6789"}
print(list(string.items()))
print(list(string.values()))
print(list(string.keys()))

word = list("antidisestablishmentarianism")
word.sort()
join_word = "".join(word)
print(join_word)
print("the quick brown fox jumped over the lazy dog".split())