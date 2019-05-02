
from netmiko import ConnectHandler

def ssh_command(device,sh_cmd):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(sh_cmd)

    print("-"*20)
    print(output)
    print("-"*20)
    print("\n\n")
    
    net_connect.disconnect()
    return output


def ssh_command2(device,sh_cmd):
    
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(sh_cmd)
    net_connect.disconnect()
    return output
