from urllib import request
import json

url = "http://official-joke-api.appspot.com/random_joke"
r = request.urlopen(url)
print(r.getcode())
data = r.read()
json_data = json.loads(data)
print(json_data)


