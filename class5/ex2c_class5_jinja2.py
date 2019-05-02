from jinja2 import Template
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import nxos1, nxos2
import time

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates"])

template_config = {}


input_vars_nxos1 = {
    "interf1": "Ethernet2/1",
    "ip1": "10.1.10.10",
    "netmask1": "24",
    "nei_ip": "10.1.10.11",
    "as_number": "22",
}
input_vars_nxos2 = {
    "interf1": "Ethernet2/1",
    "ip1": "10.1.10.11",
    "netmask1": "24",
    "nei_ip": "10.1.10.10",
    "as_number": "22",
}

for device in (nxos1, nxos2):
    input_template_file = "ex2b_class5_template.j2"
    template = env.get_template(input_template_file)
    if device == nxos1:
        cfg = template.render(**input_vars_nxos1)
        print(f"cfg for nxos1 is {cfg}")
    else:
        cfg = template.render(**input_vars_nxos2)
        print(f"cfg for nxos2 is {cfg}")

    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    print("Before applying changes")
    print(net_connect.send_command("show running-config interface Ethernet2/1"))
    print(net_connect.send_command("show running-config bgp"))
    net_connect.send_config_set(cfg)

    print("after applying changes")
    print(net_connect.send_command("show running-config interface Ethernet2/1"))
    print(net_connect.send_command("show running-config bgp"))

    net_connect.disconnect()

print("Tool sleeping for 15 seconds")
time.sleep(15)

# Check for bgp neighborship & ping

net_connect = ConnectHandler(**nxos1)
show_bgp = net_connect.send_command("show ip bgp neighbors", use_textfsm=True)

if show_bgp[0]["bgp_state"] == "Established":
    print("BGP neighborship successfully established")

ping = net_connect.send_command("ping " + input_vars_nxos1["nei_ip"])
if "64 bytes from " in ping:
    print("ping is successful")
