import yaml
from os import path
from pprint import pprint
from netmiko import ConnectHandler
home_dir=path.expanduser("~")

filename = path.join(home_dir,".netmiko.yml")

with open( filename ) as f:
    yaml_data=yaml.load(f)

pprint (yaml_data)


cisco_data=yaml_data['cisco3']


net_connect=ConnectHandler(**cisco_data)

print (net_connect.find_prompt())

net_connect.disconnect()
