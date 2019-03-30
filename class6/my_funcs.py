import yaml

def input_devices():

    filename="arista_devices_input.yml"
    with open(filename, "r") as f:
        devices=yaml.safe_load(f)
    return devices



def filter_output(output):
    for item in output[0]['result']['ipV4Neighbors']:
        print(f"IP address: {item['address']} , MAC address: {item['hwAddress']}")
