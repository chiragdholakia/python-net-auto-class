import yaml

input_list=[{"device_name":"cisco_ios1","host":"cisco1.lasthop.io","username":"demo","password":"demo"},
            {"device_name":"nx_os1","host":"nxos1.lasthop.io","username":"demo","password":"demo"},
	    {"device_name":"nx_os2","host":"nxos2.lasthop.io","username":"demo","password":"demo"},
	    {"device_name":"cisco_ios2","host":"cisco2.lasthop.io","username":"demo","password":"demo"}]



filename ="output_yaml_ex2.yml"


with open(filename, "wt") as f:
	yaml.dump(input_list,f, default_flow_style=False)
