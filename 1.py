import requests
import base64
import json

response = requests.get("https://randomuser.me/api/?nat=us&results=500&seed=abc")
print("Status code is {}".format(response))
response_body = response.json()['results']
#print(response_body)
#print(type(response_body))
dashboards = eval(response.content)

#print("\n", dashboards)
print("\n", type(dashboards))

d = dict(dashboards)

print(d)

d1 = d.values()
print(d1)

d2 = list(d1)
print(d2)
print(type(d2))

response_dict = json.loads(response_body)
titles = [entry['title'] for entry in response_dict]
print(titles)