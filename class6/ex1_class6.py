import pyeapi
from getpass import getpass
#import ipdb


connection = pyeapi.client.connect(
	transport="https",
	host="arista3.lasthop.io",
	username="pyclass",
	password=getpass(),
	port="443"
)

device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")

print(output)


for item in output[0]['result']['ipV4Neighbors']:
	print(f"IP address: {item['address']} , MAC address: {item['hwAddress']}")
