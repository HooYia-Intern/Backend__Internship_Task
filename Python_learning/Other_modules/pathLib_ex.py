from pathlib import Path

# Create a path object
p = Path('pathlib.txt')

# Check if the file exists
print("File exists:", p.exists())

# Create an empty file
p.write_text('Hello, World!')
