import re

with open("input.txt", "r") as file:
    text = file.read()

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)
emails = list(dict.fromkeys(emails))
print("Email addresses found:")

for email in emails:
    print(email)

print("Total emails found:", len(emails))

with open("output.txt", "w") as file:
    file.write("\n".join(emails))