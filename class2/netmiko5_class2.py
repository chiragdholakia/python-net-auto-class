from netmiko import ConnectHandler
from getpass import getpass
import time

nxos1_details = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}
nxos2_details = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}


for device in [nxos1_details, nxos2_details]:

    before = time.time()
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())

    # cfg_commands=["logging buffered 20000","ip name-server 1.1.1.1","ip name-server 1.0.0.1","ip domain-lookup"]

    output = net_connect.send_config_from_file(config_file="cfg_commands.txt")
    print(output)
    output_show = net_connect.send_command("show vlan")
    print(output_show)
    after = time.time()

    print(f"Time taken for execution:{after-before}")
    save_config = net_connect.save_config()
    print(save_config)
    net_connect.disconnect()
