import datetime

# Get current date and time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Format date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
