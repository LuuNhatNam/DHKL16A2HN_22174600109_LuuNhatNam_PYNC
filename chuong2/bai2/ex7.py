import json

python_object = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(python_object)

print(json_string)

parsed_object = json.loads(json_string)

for key, value in parsed_object.items():
    print(f"{key}: {value}")