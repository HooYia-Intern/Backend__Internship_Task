import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Write JSON data to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON data from the file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("Loaded JSON data:", loaded_data)
