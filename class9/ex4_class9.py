#!/user/bin/env python
from getpass import getpass
from napalm import get_network_driver
from my_devices import nxos1
from my_functions import open_napalm_conn, create_checkpoint


if __name__ == "__main__":
    conn = open_napalm_conn(nxos1)
    create_checkpoint(conn)
    
    #Stage config file
    print("Load config change - replace ")
    conn.load_replace_candidate(filename="nxos_checkpoint.txt")
    print(conn.compare_config())

    #Discard config

    conn.discard_config()
    print("Changes after discarding config")
    print(conn.compare_config())
    

