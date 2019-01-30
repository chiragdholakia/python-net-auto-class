from netmiko import ConnectHandler
from getpass import getpass

cisco_nx1={
	'device_type':'cisco_nxos',
	'host':'nxos1.lasthop.io',
	'username':'pyclass',
	'password':getpass(),
	'session_log':'session1_exercise1.txt'
}

net_connect=ConnectHandler(**cisco_nx1)
print (net_connect.find_prompt())
net_connect.disconnect()
