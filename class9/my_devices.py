from getpass import getpass
password=getpass()
cisco3={
    "hostname":"cisco3.lasthop.io",
    "device_type":"ios", 
    "username":"pyclass",
    "password":password
}

arista1={
    "hostname":"arista1.lasthop.io",
    "device_type":"eos",
    "username":"pyclass",
    "password":password
}

nxos1={
    "hostname":"nxos1.lasthop.io",
    "device_type":"nxos",
    "username":"pyclass",
    "password":password,
    "optional_args":{"port":8443}

}






network_devices = [cisco3,arista1,nxos1]

