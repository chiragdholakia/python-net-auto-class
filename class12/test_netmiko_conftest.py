def test_prompt(netmiko_conn):
    assert netmiko_conn.find_prompt() == "arista1#"


def test_show_ver(netmiko_conn):
    assert "4.20.10M" in netmiko_conn.send_command("show version")
