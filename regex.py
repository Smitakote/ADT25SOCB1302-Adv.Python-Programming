import re

# Read data from a text file
with open("input.txt", "r") as file:
    text = file.read()

# Regular expression to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find email addresses
emails = re.findall(pattern, text)

# Remove duplicate emails
emails = list(dict.fromkeys(emails))

# Display the result
print("Email addresses found:")

for email in emails:
    print(email)

print("Total emails found:", len(emails))

# Save emails to another file
with open("output.txt", "w") as file:
    file.write("\n".join(emails))