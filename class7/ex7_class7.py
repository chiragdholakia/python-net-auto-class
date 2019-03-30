from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False
)


#Ex7a
int_output = device.show("show interface Ethernet2/1")
print("\n\n")
print("Collect and parse ETH2/1 info")

print("Interface:{}; state:{}; MTU:{}".format (int_output.find(".//interface").text,
      int_output.find(".//state").text,
      int_output.find(".//eth_mtu").text)
)


#Ex7b
print("\n\n")
print("Collect XML output from multiple show commands")
show_output = device.show_list(["show system uptime","show system resources"])
for item in show_output:
    print(etree.tostring(item))


#Ex7c
print("\n\n")
commands=[
    "interface loopback151",
    "description loopback151",
    "no shutdown",
    "interface loopback155",
    "description loopback155",
    "no shutdown"
]
output = device.config_list(commands)

for item in output:
    print(etree.tostring(item).decode())

