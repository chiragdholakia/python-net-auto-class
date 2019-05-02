import time
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import network_devices


def ssh_command(device, sh_cmd):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(sh_cmd)
    net_connect.disconnect()
    return output


if __name__ == "__main__":
    start_time = time.time()
    for device in network_devices:
        output = ssh_command(device, "show version")
        print("-" * 20)
        print(output)
        print("-" * 20)
        print("\n\n")
    end_time = time.time()
    print(f"Code finished execution in {end_time-start_time:.2f} seconds")
