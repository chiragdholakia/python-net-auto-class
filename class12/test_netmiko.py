import pytest
from getpass import getpass
from netmiko import ConnectHandler

def netmiko_conn():
    
    arista1={       
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
}
    return ConnectHandler(**arista1)
  
 

def test_prompt():
    conn = netmiko_conn()
    assert conn.find_prompt() == "arista1#"

def test_show_ver():
    conn = netmiko_conn()
    assert "4.20.10M" in conn.send_command("show version")


if __name__ == "__main__":
    test_prompt()
    show_ver()
