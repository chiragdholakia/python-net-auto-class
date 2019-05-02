import json
from pprint import pprint

filename = input("Enter input json file")

with open(filename) as f:
    data = json.load(f)


pprint(data)

dict_op = {}
temp = data["ipV4Neighbors"]
for item in temp:
    mac = item["hwAddress"]
    ip = item["address"]
    dict_op[ip] = mac


print(dict_op)
