import json
import yaml

# Example of JSON

x = '{"name": "John", "age": "30", "city": "New York City"}'

# Parse JSON

y = json.loads(x)
print("THe output of json file is ", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["city"])