import re

text = "The quick brown fox jumps over the lazy dog."
pattern = input('Enter the pattern to find in the text {text}'.format(text=text))

# Search for the pattern
if re.search(pattern, text):
    print(f"'{pattern}' found in the text.")
else:
    print(f"'{pattern}' not found in the text.")
