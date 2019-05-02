import requests
import os
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]
    url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # IP address to add
    post_data = {"address": "192.0.2.125/32"}

    response = requests.post(
        url, headers=http_headers, data=json.dumps(post_data), verify=False
    )

    pprint(response.json())

    addr_id = response.json()["id"]

    # New URL specific for newly creted IP address object
    new_url = "https://netbox.lasthop.io/api/ipam/ip-addresses/" + str(addr_id) + "/"

    modified_response = requests.get(new_url, headers=http_headers, verify=False)

    pprint(modified_response.json())
