from netmiko import ConnectHandler
from getpass import getpass
import time

cisco_details = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}
net_connect = ConnectHandler(**cisco_details)
print(net_connect.find_prompt())

output_command1 = net_connect.send_command("show lldp neighbors", use_textfsm=True)
output_command2 = net_connect.send_command("show version", use_textfsm=True)
print(output_command1)
print(output_command2)
print("\n\n")
print(f"Type of DataStructure:{type(output_command1)}")
print(f"Port number of remote device:{output_command1[0]['neighbor_interface']}")


net_connect.disconnect()
