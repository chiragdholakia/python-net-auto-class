import os
import requests
import json
from pprint import pprint


from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Constant from previous script
BASE_URL = "https://netbox.lasthop.io/api/"
ADDRESS_ID = "72"


if __name__ == "__main__":

    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    put_data = {
        "address": "192.0.2.125/32",
        "description": "Testing PUT operation for REST_API",
    }

    resp = requests.put(
        f"{BASE_URL}ipam/ip-addresses/{ADDRESS_ID}/",
        headers=http_headers,
        verify=False,
        data=json.dumps(put_data),
    )

    print("Response code:", resp.status_code)
    print("JSON data")
    pprint(resp.json())
