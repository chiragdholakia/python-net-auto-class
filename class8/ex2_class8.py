from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from getpass import getpass
from pprint import pprint

from jnpr_devices import srx2


def check_connected(jnpr_connection):
    print(jnpr_connection.connected)


def gather_routes(jnpr_connection):
    routes = RouteTable(jnpr_connection)
    routes.get()
    return routes


def gather_arp_table(jnpr_connection):
    arp = ArpTable(jnpr_connection)
    arp.get()
    return arp


def print_output(jnpr_connection, route_table, arp_table):
    print("Hostname:", jnpr_connection.hostname)
    print("NETCONF Port:", jnpr_connection.port)
    print("User:", jnpr_connection.user)
    print("Route Table", route_table.items())
    print("ARP Table", arp_table.items())


if __name__ == "__main__":
    jnpr_device = Device(**srx2)
    jnpr_device.open()

    check_connected(jnpr_device)
    route_table = gather_routes(jnpr_device)
    arp_table = gather_arp_table(jnpr_device)
    print_output(jnpr_device, route_table, arp_table)
