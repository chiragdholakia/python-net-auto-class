from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint
from lxml import etree
from jnpr_devices import srx2


# get-software-information


jnpr_device = Device(**srx2)
jnpr_device.open()

# Ex5a
xml_out = jnpr_device.rpc.get_software_information()
print("show version")
print(etree.tostring(xml_out).decode())


# Ex5b
# get-interface-information
xml_out = jnpr_device.rpc.get_interface_information()
print("\n\nshow interfaces terse")
print(etree.tostring(xml_out).decode())

# Ex5c

xml_out = jnpr_device.rpc.get_interface_information(
    interface_name="fe-0/0/7", terse=True, normalize=True
)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
