import requests
import pprint

r = requests.get('https://www.boredapi.com/api/activity')
print(r.json())
pprint.pprint(r.json())