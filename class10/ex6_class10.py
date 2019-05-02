import time
from concurrent.futures import ProcessPoolExecutor,as_completed
from datetime import datetime
from my_devices import network_devices
from my_functions import ssh_command2

if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4
    
    #Using context manager to gracefully close the pool
    with ProcessPoolExecutor(max_threads) as pool:    
        future_list = []
        cmds_list=[]
        for device in network_devices:
            if "junos" in device["device_type"]:
                cmds_list.append("show arp")
            else:
                cmds_list.append("show ip arp")
            results = pool.map(ssh_command2, network_devices, cmds_list)
        
        for result in results:
            print("-"*20)
            print("Result:" + result)
            print("-"*20)
            print("\n\n")

    end_time = datetime.now()
    print(f"Elapsed time {end_time-start_time}")
    
