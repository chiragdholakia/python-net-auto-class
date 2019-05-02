import json
from pprint import pprint

ipv4_list = []
ipv6_list = []
filename = input("Enter input json file:")

with open(filename) as f:
    data = json.load(f)

pprint(data)
for key_int, value_int in data.items():

    for key_ip, value_ip in value_int.items():
        if key_ip == "ipv4":
            for value_ipv4, prefix_ipv4 in value_ip.items():
                ipv4_list.append(
                    "{}/{}".format(value_ipv4, prefix_ipv4["prefix_length"])
                )
        if key_ip == "ipv6":
            for value_ipv6, prefix_ipv6 in value_ip.items():
                ipv6_list.append(
                    "{}/{}".format(value_ipv6, prefix_ipv6["prefix_length"])
                )


print(ipv4_list)
print(ipv6_list)
