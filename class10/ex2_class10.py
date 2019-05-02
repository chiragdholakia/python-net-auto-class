#!/usr/bin/env python

import threading
from datetime import datetime
from my_devices import network_devices
from my_functions import ssh_command


if __name__ == "__main__":
    
    start_time = datetime.now()
    
    for device in network_devices:
        my_thread = threading.Thread(target=ssh_command, args=(device,"show version",))
        my_thread.start()
    

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()
    
    print(f"Elapsed time: {datetime.now() - start_time}")


