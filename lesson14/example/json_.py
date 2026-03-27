import json

# dict1 = {'key1':'val1', 'key2':'val2'}

# with open('123.json', 'w') as f:
#     json.dump(dict1, f)
    
with open('123.json', 'r') as f:
    dict2 = json.load(f)
    
# print(dict2, dict2['key1'])

print(dict2, type(dict2))

