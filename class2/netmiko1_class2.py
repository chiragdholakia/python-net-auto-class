from netmiko import ConnectHandler
from getpass import getpass

cisco_details = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco_details)
print(net_connect.find_prompt())

command = "ping"
command_expect = [
    r"Protocol",
    r"Target IP",
    r"Repeat count",
    r"Datagram size",
    r"Timeout in seconds",
    r"Extended commands",
    r"Sweep range of sizes",
    "#",
]
command_response = ["\n", "8.8.8.8\n", "10", "\n", "2", "n", "n"]


output = net_connect.send_command(command, expect_string=command_expect[0])
for i in range(len(command_response)):
    output += net_connect.send_command(
        command_response[i], expect_string=command_expect[i + 1]
    )

net_connect.disconnect()
