import json

data = {
  "firstName": "Jane",
  "lastName": "Doe",
  "hobies": ["running", "sky diving", "singing"]
}
with open("hobbies.json", "w") as write_file:
    json.dump(data, write_file)
json_string = json.dumps(data)


print(f" {json_string}")