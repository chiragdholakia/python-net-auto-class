from netmiko import ConnectHandler
from getpass import getpass

list_hostnames=['nxos1.lasthop.io','nxos2.lasthop.io']

for host_input in list_hostnames:
	print (f"Enter password for host {host_input}") 
	cisco_nx={
		'device_type':'cisco_nxos',
		'host':host_input,
		'username':'pyclass',
		'password':getpass(),
		'session_log':'session1_excercise1.txt'
}

	net_connect=ConnectHandler(**cisco_nx)
	print (net_connect.find_prompt())
	net_connect.disconnect()
