import pyeapi
import yaml
from getpass import getpass


filename = "arista_devices_input.yml"
with open(filename, "r") as f:
    devices = yaml.load(f)

print(devices.items())

for name, device_dict in devices.items():
    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")


for item in output[0]["result"]["ipV4Neighbors"]:
    print(f"IP address: {item['address']} , MAC address: {item['hwAddress']}")
