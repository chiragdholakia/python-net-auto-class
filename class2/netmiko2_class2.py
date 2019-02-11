from netmiko import ConnectHandler
from getpass import getpass
import time  
cisco_details={
    "host":"nxos2.lasthop.io",
    "username":"pyclass",
    "password":getpass(),
    "device_type":"cisco_nxos",
   # "global_delay_factor":2
}
net_connect=ConnectHandler(**cisco_details)
print (net_connect.find_prompt())
start=time.time()

output=net_connect.send_command("show lldp neighbors detail",delay_factor=2)
end=time.time()
print(f"time for global delay is {end-start}")
print (output)



net_connect.disconnect()

