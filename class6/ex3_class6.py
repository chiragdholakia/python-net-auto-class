import pyeapi
import yaml
from getpass import getpass
from my_funcs import input_devices, filter_output
from pprint import pprint


devices = input_devices()
for name, device_dict in devices.items():
    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip route")
    print(output)

for item in output[0]["result"]["vrfs"]["default"]["routes"].items():
    pprint(f"Route entry: {item[0]},   Route type:{item[1]['routeType']} ")
    if item[1]["routeType"] == "static":
        print(f"\t\tnext hop:{item[1]['vias'][0]['nexthopAddr']}")
