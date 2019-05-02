#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver
from my_devices import network_devices


# device_type = cisco.pop("device_type")
# driver = get_network_driver(device_type)
# device = driver(**cisco)

# print(device)


def open_napalm_conn(input_device):

    device_type = input_device.pop("device_type")
    driver = get_network_driver(device_type)
    conn = driver(**input_device)
    conn.open()
    return conn


if __name__ == "__main__":

    list_connections = []

    for device in network_devices:
        conn = open_napalm_conn(device)
        list_connections.append(conn)

    for conn in list_connections:
        print("device is", conn.device)
        print("platform is", conn.platform)
        pprint(conn.get_facts())
        print("-----------------")
        conn.close()
