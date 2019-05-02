
#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices
from my_functions import open_napalm_conn,create_backup



if __name__ == "__main__":
    list_connections=[]
    for input_device in network_devices:
        conn = open_napalm_conn(input_device)
        list_connections.append(conn)


    for conn in list_connections:
        pprint(conn.platform)

        #Get ARP Table information
        pprint(conn.get_arp_table())
        print("----------------------------------")

        #get NTP Peer information
        try:
            ntp_peers = conn.get_ntp_peers()
            print("NTP Peers are:",ntp_peers)
        except NotImplementedError:
            print(f"This feature is not implemented for {conn.platform} device")

        #Create backup of running config
        create_backup(conn)



