import json
with open("hobbies.json", "r") as read_file:
    data = json.load(read_file)
    hobies = data["hobies"]
    s = " , "
    s = s.join(hobies)
    firstname = data["firstName"]
    print(f"{firstname} has hobies as {s}")




