import json
import requests
r = requests.get('https://api.github.com/networks/vuetifyjs/vuetify/events')
x = r.json()
print (x)
# with open('test.json') as f:
#   data = json.load(f)

# print(json.dumps(data, indent = 4, sort_keys=True))

# print (data[0]["actor"]['login'])