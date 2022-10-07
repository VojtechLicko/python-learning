import json
from urllib import request

url = "https://v2.jokeapi.dev/joke/Any"
r = request.urlopen(url)
print(r.getcode())
data = r.read()
json_data = json.loads(data)
print(json_data)
