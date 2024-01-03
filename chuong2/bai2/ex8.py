import json
sorted_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open("output.json", "w") as json_file:
    json.dump(sorted_dict, json_file, indent=4)
with open("output.json", "r") as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent=4))