import pyeapi
import yaml
from getpass import getpass
from my_funcs import input_devices, filter_output
from pprint import pprint
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

arista_devices = []

# Load Jinja2 template

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
template_file = "arista_config_template.j2"
template = env.get_template(template_file)


devices = input_devices()
pprint(devices)
for name, device_dict in devices.items():
    device_dict["password"] = getpass()
    # Generate device config from template
    device_config = template.render(**device_dict["data"])
    device_config = device_config.strip()
    device_config = device_config.splitlines()
    print(device_config)

    # Push config to Arista devices
    connection = pyeapi.client.connect(**device_dict)
    device_obj = pyeapi.client.Node(connection)
    arista_devices.append(device_obj)
    output_config = device_obj.config(device_config)


# Validate config on devices
for device_obj in arista_devices:
    pprint(device_obj.enable("show hostname")[0]["result"]["hostname"])
    output = device_obj.enable("show ip interface brief")
    pprint(output[0]["result"]["output"])
