import pyeapi
import yaml
from getpass import getpass
from my_funcs import input_devices, filter_output


devices = input_devices()
for name, device_dict in devices.items():
    device_dict["password"] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")
    filter_output(output)
