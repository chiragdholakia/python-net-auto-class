from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

jnpr_device = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
jnpr_device.open()
device_facts = jnpr_device.facts
pprint(device_facts)
print("Hostname:", device_facts["hostname"])
