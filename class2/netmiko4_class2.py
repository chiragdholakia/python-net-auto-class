from netmiko import ConnectHandler
from getpass import getpass
import time
cisco_details={
    "host":"cisco4.lasthop.io",
    "username":"pyclass",
    "password":getpass(),
    "device_type":"cisco_ios",
    "fast_cli":True
}

before=time.time()
net_connect=ConnectHandler(**cisco_details)
print (net_connect.find_prompt())

cfg_commands=["logging buffered 20000","ip name-server 1.1.1.1","ip name-server 1.0.0.1","ip domain-lookup"]

output=net_connect.send_config_set(cfg_commands)
print (output)
output_show=net_connect.send_command("ping google.com")
print (output_show)
after=time.time()

print (f"Time taken for execution:{after-before}")
net_connect.disconnect()

