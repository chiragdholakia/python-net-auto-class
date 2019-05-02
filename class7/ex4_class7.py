from lxml import etree

with open("show_security_zones.xml", "r") as input_file:
    show_security = etree.fromstring(input_file.read())

# print(show_security)
# print(type(show_security))

# my_xml = etree.tostring(show_security).decode()
# Ex-4a
print("Find tag of the first zones-security element ")
print("--------------------")
zones_sec = show_security.find("zones-security")
print(zones_sec.tag)

print("\nFind tag of all child elements of the first zones-security element")
print("--------------------")

for child in zones_sec.iterchildren():
    print(child.tag)


# Ex-4b

print("\nZone name:", zones_sec.find("zones-security-zonename").text)


# Ex-4c

all_zones_sec = show_security.findall(".//zones-security")
print("\nzonenames for all zones-security:")

for zone in all_zones_sec:
    print(zone.find("zones-security-zonename").text)
