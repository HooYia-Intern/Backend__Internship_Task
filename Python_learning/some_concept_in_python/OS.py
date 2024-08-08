import os

filename = "example.txt"

# Check if the file exists
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("This is a new file.")
    print(f"File '{filename}' created.")
else:
    print(f"File '{filename}' already exists.")
