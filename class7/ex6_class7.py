from getpass import getpass
from nxapi_plumbing import Device

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet2/1")

print(
    f"Interface: {output['TABLE_interface']['ROW_interface']['interface']}; \
      State: {output['TABLE_interface']['ROW_interface']['state']}; \
      MTU: {output['TABLE_interface']['ROW_interface']['eth_mtu']}"
)

# print(output)
