from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass
from pprint import pprint

from jnpr_devices import srx2
from ex2_class8 import gather_routes

def conf_file(jnpr_conn):
    cfg = Config(jnpr_conn)
    cfg.lock()
    cfg.load(path="jnpr_config.conf",format="text",merge="True")
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()

def compare_routes(initial_routes,updated_routes):
    diff_routes=[]
    for iter in range(0,len(updated_routes)):
        if updated_routes[iter] not in initial_routes:
            diff_routes.append(updated_routes[iter])
    print("diff in routes",diff_routes)


def delete_routes(jnpr_conn):
    cfg = Config(jnpr_conn)
    cfg.lock()
    cfg.load("delete routing-options static route 203.0.113.50/32 ",format="set",merge="True")
    cfg.load("delete routing-options static route 203.0.113.100/32 ",format="set",merge="True")
    if cfg.diff() is not None:
        cfg.commit()
    cfg.unlock()


if __name__ == "__main__":
    jnpr_device = Device(**srx2)
    jnpr_device.open()
    jnpr_device.timeout = 60

#Collect initial route table info
    initial_routes = gather_routes(jnpr_device)
    pprint(initial_routes.keys())

#Configure Static routes
    conf_file(jnpr_device)

#Collect updated route table info
    updated_routes = gather_routes(jnpr_device)
    pprint(updated_routes.keys())

#Diff initial and updated route table
    print("Diff after adding static route config")
    compare_routes(initial_routes.keys(),updated_routes.keys())

#Cleanup of static route config
    delete_routes(jnpr_device)

#Diff initial and updated route table
    print("Diff after deleting static route config")
    compare_routes(initial_routes.keys(),updated_routes.keys())


