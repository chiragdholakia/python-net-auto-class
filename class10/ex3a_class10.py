import time
from concurrent.futures import ThreadPoolExecutor,wait
from datetime import datetime
from my_devices import network_devices
from my_functions import ssh_command2

if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 4
    
    pool = ThreadPoolExecutor(max_threads)
    
    future_list = []
    for device in network_devices:
        future = pool.submit(ssh_command2,device,"show version")
        future_list.append(future)

    wait(future_list)

    
    for future in future_list:
        print("-"*20)
        print("Result:" + future.result())
        print("-"*20)
        print("\n\n")

    end_time = datetime.now()
    print(f"Elapsed time {end_time-start_time}")
    
