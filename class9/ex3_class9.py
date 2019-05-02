
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
    
        print("Load config change without commit")
        if conn.platform =="ios":
            conn.load_merge_candidate(filename="cisco3.lasthop.io-loopbacks")
            print(conn.compare_config())
    

        if conn.platform =="eos":
            conn.load_merge_candidate(filename="arista1.lasthop.io-loopbacks")
            print(conn.compare_config())


        print ("Commit config chanfge")
        conn.commit_config()
        print("Diff after commit")

        print(conn.compare_config())
