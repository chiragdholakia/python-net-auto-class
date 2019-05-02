from netmiko import ConnectHandler
from getpass import getpass

ios_device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**ios_device)

output = net_connect.send_command("show version")

print(output)


with open("sh_ver_output.txt", "w+") as f:
    f.write(output)

net_connect.disconnect()
