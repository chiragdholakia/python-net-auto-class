import os
import requests

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Constant from previous script
BASE_URL = "https://netbox.lasthop.io/api/"
ADDRESS_ID = "71"

if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]
    url = f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/"

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    resp = requests.delete(url, headers=http_headers, verify=False)

    print(resp)

    if resp.ok:
        print("Device deleted successfully")
