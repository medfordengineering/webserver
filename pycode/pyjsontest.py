import json

with open('distro.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)
