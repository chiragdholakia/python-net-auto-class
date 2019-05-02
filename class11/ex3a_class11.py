import requests
import os
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/dcim/devices"

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"
    response = requests.get(url, headers=http_headers, verify=False)

    print("Status code:", response.status_code)

    print("Devices under /api/dcim/devices")
    resp = response.json()["results"]
    for iter in range(len(resp)):
        print(resp[iter]["display_name"])
