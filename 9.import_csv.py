import csv
import json

# Read data from the CSV file
with open("input.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Convert CSV data into JSON format
json_data = json.dumps(data, indent=4)

# Write JSON data into the output file
with open("output.json", "w") as file:
    file.write(json_data)

print("CSV data converted into JSON successfully!")
print("Total records converted:", len(data))