import pytest
from getpass import getpass
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def netmiko_conn(request):

    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }
    net_connect = ConnectHandler(**arista1)

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect
