import json

with open('test.json') as f:
  data = json.load(f)

# print(json.dumps(data, indent = 4, sort_keys=True))

print (data)