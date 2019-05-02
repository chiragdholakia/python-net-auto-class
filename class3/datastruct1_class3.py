from pprint import pprint


arp_data = """Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

print(arp_data)

arp_data_list = arp_data.split("\n")
fin_list = []
for element in range(1, len(arp_data_list) - 1):
    temp_list = arp_data_list[element].split()
    dict_temp = {}
    dict_temp["mac_addr"] = temp_list[3]
    dict_temp["ip_addr"] = temp_list[1]
    dict_temp["interface"] = temp_list[5]
    fin_list.append(dict_temp)

pprint(fin_list)
