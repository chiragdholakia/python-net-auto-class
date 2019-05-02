from napalm import get_network_driver


def open_napalm_conn(input_device):

    device_type = input_device.pop("device_type")
    driver = get_network_driver(device_type)
    conn = driver(**input_device)
    print("Opening connection to test device")
    conn.open()
    return conn


def create_backup(conn):
    run_config = conn.get_config()
    

    filename = "running_config_"+conn.hostname+".txt" 
    with open(filename , "w") as f:
        f.write(run_config['running'])


def create_checkpoint(conn):
    print("creating checkpoint file")
    filename = conn.hostname+"_checkpoint_file.txt"
    with open(filename,"w") as f:
        f.write(conn._get_checkpoint_file())


