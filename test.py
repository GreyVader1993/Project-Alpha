import json
import requests
from pprint import pprint

# print('User (case-sensitive):')
# x1 = input()
# print('Repository (case-sensitive):')
# x2 = input()

r = requests.get('https://api.github.com/networks/'+'GreyVader1993'+'/'+'Project-Alpha'+'/events')
x = r.json()
pprint (x[0]["actor"]['login'])



# with open('test.json') as f:
#   data = json.load(f)

# print(json.dumps(data, indent = 4, sort_keys=True))

# print (data[0]["actor"]['login'])