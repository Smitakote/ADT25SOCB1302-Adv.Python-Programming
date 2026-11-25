
import re

f = open("story.txt", "r")
text = f.read()
f.close()

words = re.findall(r'\b\w+(?:ing|ed)\b', text)

f = open("matching_words.txt", "w")

for word in words:
    f.write(word + "\n")

f.close()

print("Matching words saved successfully!")





