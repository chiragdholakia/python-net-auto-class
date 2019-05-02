import yaml
from os import path
from pprint import pprint
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")

filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_data = yaml.load(f)

pprint(yaml_data)


cisco_data = yaml_data["cisco4"]


net_connect = ConnectHandler(**cisco_data)

print(net_connect.find_prompt())

run_config = net_connect.send_command("show run")

with open("cisco.txt", "wt") as f:
    f.write(run_config)
net_connect.disconnect()

cisco_obj = CiscoConfParse("cisco.txt")

match = cisco_obj.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
)

interface = {}

for item in match:
    # interface.append(item.text)
    interface[item.text] = item.children[0].text

print(interface)


for key, value in interface.items():
    print("Interface Line: ", key)
    print("IP Address Line: ", value)
