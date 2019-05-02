import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__ == "__main__":

    url = "https://netbox.lasthop.io/api/dcim"
    http_headers= {"accept":"application/json; version=2.4;"}
    response = requests.get(url, headers=http_headers, verify=False)
    
    print("Status code:",response.status_code)

    print("Child endpoints under DCIM:")
    pprint(response.json())

