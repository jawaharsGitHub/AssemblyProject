import json

def get_districts():
    with open("RevDistrict.json", 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        return data

# print(get_districts())